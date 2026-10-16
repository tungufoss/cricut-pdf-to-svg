"""Existing raster-to-vector methods, each wrapped to return a Prediction in mm.

A  contours:   Otsu threshold, OpenCV contour tracing, Douglas-Peucker. Filled outlines.
B  potrace:    Potrace (the engine behind Inkscape's Trace Bitmap). Filled Bezier outlines.
C  centerline: Zhang-Suen thinning, chains split at junctions, Douglas-Peucker. Stroked
               centrelines, the classical technical-drawing approach.

None of them knows cut from fold; classify.py labels their paths afterwards.
"""

from __future__ import annotations

import sys
from pathlib import Path

import cv2
import numpy as np
import potrace

from .model import Polyline, Prediction

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.lowpoly_pdf_to_svg.skeleton import paths_from_skeleton, simplify, thin  # noqa: E402


def ink(gray: np.ndarray) -> np.ndarray:
    """Dark artwork as a boolean mask (Otsu threshold)."""
    _, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return mask > 0


class Vectorizer:
    name = "?"
    filled = True            # True: paths are outlines of ink regions; False: centrelines

    def __call__(self, gray: np.ndarray, dpi: int) -> Prediction:
        mm = 25.4 / dpi
        paths = self.trace(gray, mm)
        pred = Prediction(self.name, paths, filled=self.filled)
        pred.svg_bytes = len(pred.to_svg(gray.shape[1] * mm, gray.shape[0] * mm).encode())
        return pred

    def trace(self, gray: np.ndarray, mm: float) -> list[Polyline]:
        raise NotImplementedError


class Contours(Vectorizer):
    name = "A-contours"

    def trace(self, gray, mm):
        mask = ink(gray).astype(np.uint8)
        contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        paths = []
        for c in contours:
            if len(c) < 3:
                continue
            poly = cv2.approxPolyDP(c, 1.0, True)[:, 0, :]
            paths.append(Polyline([(float(x) * mm, float(y) * mm) for x, y in poly], closed=True))
        return paths


class Potrace(Vectorizer):
    name = "B-potrace"
    STEPS = 8                # points per Bezier segment when flattening

    def trace(self, gray, mm):
        # potracer traces the False pixels, so hand it the background
        plist = potrace.Bitmap(~ink(gray)).trace(turdsize=2, alphamax=1.0, opticurve=True)
        paths = []
        for curve in plist:
            pts, controls = [], 0
            cur = _xy(curve.start_point)
            for seg in curve.segments:
                end = _xy(seg.end_point)
                if seg.is_corner:
                    c = _xy(seg.c)
                    pts += [tuple(c), tuple(end)]
                    controls += 2
                else:
                    c1, c2 = _xy(seg.c1), _xy(seg.c2)
                    for t in np.linspace(0, 1, self.STEPS + 1)[1:]:
                        p = (1 - t) ** 3 * cur + 3 * (1 - t) ** 2 * t * c1 + 3 * (1 - t) * t ** 2 * c2 + t ** 3 * end
                        pts.append(tuple(p))
                    controls += 3
                cur = end
            paths.append(Polyline([(x * mm, y * mm) for x, y in pts], closed=True, controls=controls))
        return paths


def _xy(point) -> np.ndarray:
    return np.array([float(point.x), float(point.y)]) if hasattr(point, "x") else np.asarray(point, float)


class Centerline(Vectorizer):
    name = "C-centerline"
    filled = False

    def trace(self, gray, mm):
        skeleton = thin(ink(gray))
        paths = []
        for chain, _ in paths_from_skeleton(skeleton, min_length=3):
            pts = simplify([(x, y) for y, x in chain], 1.0)
            closed = len(chain) > 3 and max(abs(chain[0][0] - chain[-1][0]), abs(chain[0][1] - chain[-1][1])) <= 1
            if closed:
                pts = pts[:-1]
            paths.append(Polyline([(float(x) * mm, float(y) * mm) for x, y in pts], closed=closed))
        return paths


METHODS = [Contours(), Potrace(), Centerline()]
