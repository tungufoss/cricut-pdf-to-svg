"""Shared cut/fold classifier for methods that output untyped paths.

Decided for paper 1 (2026-10-15): every method's paths are labelled by the same rule, so
cut/fold accuracy and matching-edge consistency compare across methods. The rule looks at
the source raster along each straight segment: a solid printed line is a cut, a broken
(dashed or dash-dotted) one is a fold. A path shorter than WINDOW_MM (typically one traced
dash) is judged on a WINDOW_MM stretch of its own line, so the gaps around it count. A path
whose segments change kind is split into runs. The classifier belongs to the evaluation
protocol, not to any method.
"""

from __future__ import annotations

import numpy as np

from .baselines import ink
from .model import CUT, FOLD, Polyline, Prediction

STEP_MM = 0.2          # sampling step along a segment
BAND_MM = 0.35         # half-width searched across the segment for ink
SOLID = 0.9            # ink fraction at or above which a segment counts as solid
SHORT_MM = 1.0         # segments shorter than this inherit their neighbour's kind
WINDOW_MM = 6.0        # paths shorter than this are judged on a window this long along their line


class SharedClassifier:
    def __init__(self, gray: np.ndarray, dpi: int):
        self.mask = ink(gray)
        self.px = dpi / 25.4

    def ink_fraction(self, a, b, window: bool = False) -> float:
        a, b = np.asarray(a) * self.px, np.asarray(b) * self.px
        length = np.linalg.norm(b - a)
        if length == 0:
            return 1.0
        u = (b - a) / length
        n = np.array([-u[1], u[0]])
        grow = max(0.0, WINDOW_MM * self.px - length) / 2 if window else 0.0
        a, b, length = a - u * grow, b + u * grow, length + 2 * grow
        steps = max(2, int(length / (STEP_MM * self.px)))
        offsets = np.linspace(-BAND_MM, BAND_MM, 5) * self.px
        h, w = self.mask.shape
        hits = 0
        for t in np.linspace(0, length, steps):
            p = a + u * t + n[None, :] * offsets[:, None]
            x = np.clip(np.round(p[:, 0]).astype(int), 0, w - 1)
            y = np.clip(np.round(p[:, 1]).astype(int), 0, h - 1)
            hits += bool(self.mask[y, x].any())
        return hits / steps

    def __call__(self, pred: Prediction) -> Prediction:
        if all(p.kind for p in pred.paths):
            return pred                                    # the method typed its own paths
        out = []
        for path in pred.paths:
            pts = path.points + (path.points[:1] if path.closed else [])
            total = sum(np.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:]))
            if total < WINDOW_MM:
                # A short fragment: judge its main direction over a window of its line.
                arr = np.asarray(path.points, float)
                centre = arr.mean(axis=0)
                if len(arr) > 2:
                    _, _, vt = np.linalg.svd(arr - centre)
                    u = vt[0]
                else:
                    u = (arr[-1] - arr[0]) / max(np.linalg.norm(arr[-1] - arr[0]), 1e-9)
                kind = CUT if self.ink_fraction(centre - u * 0.01, centre + u * 0.01, window=True) >= SOLID else FOLD
                out.append(Polyline(path.points, path.closed, kind, path.controls))
                continue
            kinds = []
            for a, b in zip(pts, pts[1:]):
                long = np.hypot(b[0] - a[0], b[1] - a[1]) >= SHORT_MM
                kinds.append((CUT if self.ink_fraction(a, b) >= SOLID else FOLD) if long else None)
            known = [k for k in kinds if k]
            fill = max(set(known), key=known.count) if known else CUT
            kinds = [k or fill for k in kinds]
            if len(set(kinds)) == 1:
                out.append(Polyline(path.points, path.closed, kinds[0], path.controls))
                continue
            run = [pts[0]]                                 # split into runs of one kind
            for i, k in enumerate(kinds):
                run.append(pts[i + 1])
                if i + 1 == len(kinds) or kinds[i + 1] != k:
                    out.append(Polyline(run, False, k))
                    run = [pts[i + 1]]
        return Prediction(pred.method, out, pred.svg_bytes, pred.filled)
