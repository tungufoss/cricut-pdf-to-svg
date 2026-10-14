from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from xml.sax.saxutils import escape

import numpy as np
from PIL import Image
from pypdf import PdfReader


@dataclass
class Material:
    id: str
    name: str
    pages: list[int]


@dataclass
class Project:
    pdf: Path
    page_size: str
    sheet_size: str
    materials: list[Material]


def load_config(path: Path) -> Project:
    """Read the deliberately small, documented YAML subset used by bowser.yaml."""
    raw = path.read_text(encoding="utf-8")
    source = re.search(r"(?ms)^source:\s*\n\s+pdf:\s*(.+?)\s*\n\s+page_size:\s*(\S+)", raw)
    sheet = re.search(r"(?m)^\s+default_sheet:\s*(\S+)\s*$", raw)
    if not source or not sheet:
        raise ValueError(f"{path}: expected source.pdf, source.page_size, and output.default_sheet")
    pdf = (path.parent / source.group(1).strip().strip("'\"" )).resolve()
    page_size = source.group(2).lower()
    materials: list[Material] = []
    blocks = re.findall(r"(?ms)^  - id:\s*(\S+)\s*\n\s+name:\s*(.*?)\s*\n\s+pages:\s*\[([^]]*)\]", raw)
    for material_id, name, pages in blocks:
        parsed_pages = [int(page.strip()) for page in pages.split(",") if page.strip()]
        materials.append(Material(material_id, name.strip().strip("'\""), parsed_pages))
    if not materials:
        raise ValueError(f"{path}: no materials were found")
    return Project(pdf, page_size, sheet.group(1).lower(), materials)


def thin(binary: np.ndarray) -> np.ndarray:
    """Zhang-Suen thinning, returning one-pixel centerlines for dark artwork."""
    image = binary.copy().astype(bool)
    changed = True
    while changed:
        changed = False
        for phase in (0, 1):
            p = np.pad(image, 1)
            neighbors = [p[:-2, 1:-1], p[:-2, 2:], p[1:-1, 2:], p[2:, 2:],
                         p[2:, 1:-1], p[2:, :-2], p[1:-1, :-2], p[:-2, :-2]]
            count = sum(n.astype(np.uint8) for n in neighbors)
            transitions = np.zeros(image.shape, dtype=np.uint8)
            for idx in range(8):
                transitions += (~neighbors[idx] & neighbors[(idx + 1) % 8]).astype(np.uint8)
            common = image & (count >= 2) & (count <= 6) & (transitions == 1)
            if phase == 0:
                remove = common & ~(neighbors[0] & neighbors[2] & neighbors[4]) & ~(neighbors[2] & neighbors[4] & neighbors[6])
            else:
                remove = common & ~(neighbors[0] & neighbors[2] & neighbors[6]) & ~(neighbors[0] & neighbors[4] & neighbors[6])
            if remove.any():
                image[remove] = False
                changed = True
    return image


def paths_from_skeleton(skeleton: np.ndarray, min_length: int = 5) -> list[tuple[list[tuple[int, int]], int]]:
    """Split a thinned raster into centerline chains at endpoints and junctions."""
    points = set(map(tuple, np.argwhere(skeleton)))
    if not points:
        return []
    neighbors: dict[tuple[int, int], list[tuple[int, int]]] = {}
    for y, x in points:
        adjacent = []
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                candidate = (y + dy, x + dx)
                if not (dy or dx) or candidate not in points:
                    continue
                # Avoid creating triangular junctions where a diagonal only touches
                # an already-connected horizontal or vertical skeleton pixel.
                if dy and dx and ((y + dy, x) in points or (y, x + dx) in points):
                    continue
                adjacent.append(candidate)
        neighbors[(y, x)] = adjacent
    visited: set[tuple[tuple[int, int], tuple[int, int]]] = set()

    def edge(a: tuple[int, int], b: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
        return (a, b) if a < b else (b, a)

    chains: list[tuple[list[tuple[int, int]], int]] = []
    nodes = sorted(point for point in points if len(neighbors[point]) != 2)
    for start in nodes:
        for nxt in neighbors[start]:
            if edge(start, nxt) in visited:
                continue
            chain = [start, nxt]
            visited.add(edge(start, nxt))
            prev, current = start, nxt
            while len(neighbors[current]) == 2:
                following = neighbors[current][0] if neighbors[current][1] == prev else neighbors[current][1]
                if edge(current, following) in visited:
                    break
                visited.add(edge(current, following))
                chain.append(following)
                prev, current = current, following
            if len(chain) >= min_length:
                chains.append((chain, len(neighbors[start]) + len(neighbors[current])))

    # Closed contours have no endpoint or junction, so seed each remaining loop.
    for point in sorted(points):
        for nxt in neighbors[point]:
            if edge(point, nxt) in visited:
                continue
            chain = [point, nxt]
            visited.add(edge(point, nxt))
            prev, current = point, nxt
            while current != point:
                options = [n for n in neighbors[current] if n != prev and edge(current, n) not in visited]
                if not options:
                    break
                following = options[0]
                visited.add(edge(current, following))
                chain.append(following)
                prev, current = current, following
            if len(chain) >= min_length:
                chains.append((chain, 2))
    return chains


def simplify(points: list[tuple[int, int]], tolerance: float = 1.15) -> list[tuple[int, int]]:
    """Douglas-Peucker simplification in raster coordinates."""
    if len(points) < 3:
        return points
    a, b = np.asarray(points[0], float), np.asarray(points[-1], float)
    line = b - a
    denom = np.linalg.norm(line)
    if denom == 0:
        distances = np.linalg.norm(np.asarray(points[1:-1], float) - a, axis=1)
    else:
        values = np.asarray(points[1:-1], float) - a
        distances = np.abs(line[0] * values[:, 1] - line[1] * values[:, 0]) / denom
    if not len(distances) or float(distances.max()) <= tolerance:
        return [points[0], points[-1]]
    index = int(np.argmax(distances)) + 1
    return simplify(points[:index + 1], tolerance)[:-1] + simplify(points[index:], tolerance)


def path_data(points: list[tuple[int, int]], scale: float) -> str:
    simplified = simplify(points)
    if len(simplified) < 2:
        return ""
    commands = [f"M {simplified[0][1] * scale:.2f},{simplified[0][0] * scale:.2f}"]
    commands.extend(f"L {x * scale:.2f},{y * scale:.2f}" for y, x in simplified[1:])
    return " ".join(commands)


def render_page(pdf: Path, page: int, dpi: int, output: Path, pdftoppm: str) -> tuple[Image.Image, tuple[float, float]]:
    prefix = output.with_suffix("")
    command = [pdftoppm, "-f", str(page), "-l", str(page), "-singlefile", "-png", "-r", str(dpi), "-cropbox", str(pdf), str(prefix)]
    subprocess.run(command, check=True, capture_output=True, text=True)
    image = Image.open(output).convert("RGB")
    reader = PdfReader(str(pdf))
    box = reader.pages[page - 1].cropbox
    return image, (float(box.width), float(box.height))


def make_svg(image: Image.Image, page_points: tuple[float, float], dpi: int,
             project: Project, material: Material, page: int) -> str:
    rgb = np.asarray(image)
    # Exclude the red ink instruction from the geometric trace; retain grayscale line art.
    is_red = (rgb[:, :, 0] > rgb[:, :, 1] * 1.3) & (rgb[:, :, 0] > rgb[:, :, 2] * 1.2) & (rgb[:, :, 0] > 100)
    gray = (rgb[:, :, 0] * 0.299 + rgb[:, :, 1] * 0.587 + rgb[:, :, 2] * 0.114)
    binary = (gray < 225) & ~is_red
    skeleton = thin(binary)
    scale = 72.0 / dpi
    cut: list[str] = []
    score: list[str] = []
    # Broken, elongated centerline chains are likely dashed fold marks. Junction-connected
    # chains and closed contours remain solid cut candidates. Review this heuristic.
    for chain, junctions in paths_from_skeleton(skeleton):
        coords = np.asarray(chain, dtype=float)
        bounds = np.ptp(coords, axis=0)
        length = float(np.linalg.norm(np.diff(coords, axis=0), axis=1).sum())
        elongation = max(bounds) / max(1.0, min(bounds) + 1.0)
        data = path_data(chain, scale)
        if not data:
            continue
        if junctions <= 2 and length >= 5 and elongation >= 3.0:
            score.append(data)
        else:
            cut.append(data)

    width, height = page_points
    groups = []
    groups.append(f'<g id="cut" inkscape:label="Cut" data-operation="cut" fill="none" stroke="#000000" stroke-width="0.35" stroke-linecap="round" stroke-linejoin="round">{paths(cut)}</g>')
    groups.append(f'<g id="score" inkscape:label="Score - review detected folds" data-operation="score" fill="none" stroke="#555555" stroke-width="0.35" stroke-linecap="round" stroke-linejoin="round">{paths(score)}</g>')
    groups.append('<g id="draw" inkscape:label="Draw - add edge numbers after review" data-operation="draw" fill="none" stroke="#cc0000" stroke-width="0.35"/>')
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" '
            f'width="{width / 72:.5f}in" height="{height / 72:.5f}in" viewBox="0 0 {width:.2f} {height:.2f}">\n'
            f'<title>Bowser page {page:02d} - {escape(material.name)}</title>\n'
            f'<desc>Source PDF page {page}; traced at {dpi} dpi. Verify all paths against the included preview before cutting. Material: {escape(material.name)}. Sheet target in manifest: {escape(project.sheet_size)}.</desc>\n'
            f'<g id="item-page-{page:02d}" inkscape:label="Page {page:02d} · {escape(material.name)}" data-material="{escape(material.id)}">\n'
            + "\n".join(groups) + "\n</g>\n</svg>\n")


def paths(items: list[str]) -> str:
    return "".join(f'<path d="{item}"/>\n' for item in items)


def main() -> int:
    parser = argparse.ArgumentParser(description="Trace Bowser papercraft PDF pages into Cricut-oriented SVGs.")
    parser.add_argument("--config", type=Path, default=Path("data/bowser.yaml"), help="project YAML manifest")
    parser.add_argument("--output", type=Path, default=Path("output/bowser"), help="directory for SVGs and review PNGs")
    parser.add_argument("--dpi", type=int, default=180, help="PDF render resolution (default: 180)")
    parser.add_argument("--page", type=int, action="append", help="convert only this 1-based page; repeat to select multiple")
    parser.add_argument("--pdftoppm", default="pdftoppm", help="Poppler pdftoppm executable")
    args = parser.parse_args()
    config = args.config.resolve()
    project = load_config(config)
    if not project.pdf.is_file():
        parser.error(f"PDF not found: {project.pdf}")
    renderer = shutil.which(args.pdftoppm) or (args.pdftoppm if Path(args.pdftoppm).is_file() else None)
    if not renderer:
        parser.error("pdftoppm was not found; install Poppler and add its bin folder to PATH, or pass --pdftoppm")
    reader = PdfReader(str(project.pdf))
    selected = set(args.page) if args.page else None
    args.output.mkdir(parents=True, exist_ok=True)
    converted = 0
    seen: set[int] = set()
    for material in project.materials:
        for page in material.pages:
            if selected is not None and page not in selected:
                continue
            if page in seen:
                parser.error(f"page {page} is assigned to more than one material")
            seen.add(page)
            if page < 1 or page > len(reader.pages):
                parser.error(f"page {page} is outside the PDF's 1..{len(reader.pages)} range")
            stem = f"bowser-page-{page:02d}-{material.id}"
            png_path = args.output / "previews" / f"{stem}.png"
            png_path.parent.mkdir(parents=True, exist_ok=True)
            image, page_points = render_page(project.pdf, page, args.dpi, png_path, renderer)
            svg = make_svg(image, page_points, args.dpi, project, material, page)
            (args.output / f"{stem}.svg").write_text(svg, encoding="utf-8")
            converted += 1
            print(f"page {page:02d} -> {args.output / f'{stem}.svg'} ({material.name})")
    if selected is not None:
        missing = selected - seen
        if missing:
            parser.error(f"selected page(s) not assigned to a material in {config.name}: {', '.join(map(str, sorted(missing)))}")
    print(f"Converted {converted} page(s). Preview PNGs are in {args.output / 'previews'}.")
    print("Review each SVG and preview before cutting. Detected folds and draw labels need human confirmation.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
