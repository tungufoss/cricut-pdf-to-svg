"""Project manifest: which PDF pages are printed on which cardstock."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

# Sheet sizes in millimetres (width, height).
SHEETS_MM = {
    "a4": (210.0, 297.0),
    "letter": (215.9, 279.4),
    "12x12": (304.8, 304.8),
}


@dataclass(frozen=True)
class Material:
    id: str
    name: str
    pages: tuple[int, ...]


@dataclass(frozen=True)
class Project:
    name: str
    pdf: Path
    page_size: str
    sheet_size: str
    materials: tuple[Material, ...]

    @classmethod
    def load(cls, path: Path) -> "Project":
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        try:
            source, output = raw["source"], raw["output"]
            materials = tuple(
                Material(str(m["id"]), str(m["name"]), tuple(int(p) for p in m["pages"]))
                for m in raw["materials"]
            )
            project = cls(
                name=str(raw["project"]),
                pdf=(path.parent / source["pdf"]).resolve(),
                page_size=str(source["page_size"]).lower(),
                sheet_size=str(output["default_sheet"]).lower(),
                materials=materials,
            )
        except (KeyError, TypeError) as error:
            raise ValueError(f"{path}: missing or malformed field {error}") from error
        if not materials:
            raise ValueError(f"{path}: no materials were found")
        if project.sheet_size not in SHEETS_MM:
            raise ValueError(f"{path}: unknown sheet {project.sheet_size!r}; use one of {sorted(SHEETS_MM)}")
        return project

    def pages(self) -> list[tuple[int, Material]]:
        """Every assigned page with its material, rejecting pages listed twice."""
        seen: dict[int, Material] = {}
        for material in self.materials:
            for page in material.pages:
                if page in seen:
                    raise ValueError(f"page {page} is assigned to both {seen[page].id} and {material.id}")
                seen[page] = material
        return sorted(seen.items())
