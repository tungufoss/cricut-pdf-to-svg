"""Stage 1: render one PDF page to a raster image at a known resolution."""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image
from pypdf import PdfReader


@dataclass
class PageImage:
    number: int
    rgb: np.ndarray          # H x W x 3, uint8
    dpi: int
    size_mm: tuple[float, float]
    path: Path               # rendered PNG on disk, used as the Inkscape source layer

    @property
    def mm_per_px(self) -> float:
        return 25.4 / self.dpi


class PageRenderer:
    def __init__(self, pdf: Path, dpi: int, pdftoppm: str = "pdftoppm"):
        self.pdf = pdf
        self.dpi = dpi
        self.pdftoppm = pdftoppm
        self.reader = PdfReader(str(pdf))

    @property
    def page_count(self) -> int:
        return len(self.reader.pages)

    def render(self, page: int, png: Path) -> PageImage:
        if not 1 <= page <= self.page_count:
            raise ValueError(f"page {page} is outside the PDF's 1..{self.page_count} range")
        png.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [self.pdftoppm, "-f", str(page), "-l", str(page), "-singlefile", "-png",
             "-r", str(self.dpi), "-cropbox", str(self.pdf), str(png.with_suffix(""))],
            check=True, capture_output=True, text=True,
        )
        box = self.reader.pages[page - 1].cropbox
        size_mm = (float(box.width) * 25.4 / 72, float(box.height) * 25.4 / 72)
        rgb = np.asarray(Image.open(png).convert("RGB"))
        return PageImage(page, rgb, self.dpi, size_mm, png)
