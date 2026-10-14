"""Centerline tracing helpers for thin raster artwork such as printed edge numbers."""

from __future__ import annotations

import numpy as np


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
