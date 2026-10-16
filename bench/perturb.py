"""Ground truth as a prediction, plus controlled damage to it.

The oracle is the exact truth written as cut and fold polylines: perfect fabrication
scores, yet imperfect visual scores because it carries no printed numbers. The perturbed
variants add one kind of fabrication error each while staying visually close to the
source, which spreads the visual-vs-fabrication comparison beyond what the baselines give.
"""

from __future__ import annotations

import random

import numpy as np

from .model import CUT, FOLD, Page, Polyline, Prediction


class Oracle:
    name = "T-oracle"

    def __init__(self, seed: int = 0):
        self.rng = random.Random(seed)

    def paths(self, truth: Page) -> list[Polyline]:
        out = []
        for piece in truth.pieces:
            for ring in [piece.outline, *piece.holes]:
                out.append(Polyline(list(ring), True, CUT))
            for a, b in piece.folds:
                out.append(Polyline([a, b], False, FOLD))
        return out

    def damage(self, paths: list[Polyline], truth: Page) -> list[Polyline]:
        return paths

    def __call__(self, truth: Page) -> Prediction:
        paths = self.damage(self.paths(truth), truth)
        pred = Prediction(self.name, paths, filled=False)
        pred.svg_bytes = len(pred.to_svg(truth.width_mm, truth.height_mm).encode())
        return pred


class Scaled(Oracle):
    """Whole page scaled about its centre, as from a wrong DPI or print scaling."""
    name = "T-scale-2pct"
    factor = 1.02

    def damage(self, paths, truth):
        cx, cy = truth.width_mm / 2, truth.height_mm / 2
        f = self.factor
        return [Polyline([(cx + (x - cx) * f, cy + (y - cy) * f) for x, y in p.points], p.closed, p.kind) for p in paths]


class Jittered(Oracle):
    """Every vertex moved up to 0.4 mm, as from a sloppy tracer."""
    name = "T-jitter-0.4mm"
    amount = 0.4

    def damage(self, paths, truth):
        move = {}

        def j(q):
            if q not in move:                              # shared corners move together
                move[q] = (q[0] + self.rng.uniform(-self.amount, self.amount), q[1] + self.rng.uniform(-self.amount, self.amount))
            return move[q]
        return [Polyline([j(q) for q in p.points], p.closed, p.kind) for p in paths]


class OpenContour(Oracle):
    """Each outline left open by a 0.6 mm gap: invisible on screen, fatal on the cutter."""
    name = "T-open-gap"

    def damage(self, paths, truth):
        out = []
        for p in paths:
            if p.kind == CUT and p.closed:
                a, b = np.asarray(p.points[0]), np.asarray(p.points[1])
                u = (b - a) / np.linalg.norm(b - a)
                out.append(Polyline([tuple(a + u * 0.6), *p.points[1:], tuple(a)], False, CUT))
            else:
                out.append(p)
        return out


class FoldsAsCuts(Oracle):
    """Folds labelled as cuts: geometry perfect, semantics wrong."""
    name = "T-folds-as-cuts"

    def damage(self, paths, truth):
        return [Polyline(p.points, p.closed, CUT) for p in paths]


VARIANTS = [Oracle(), Scaled(), Jittered(1), OpenContour(), FoldsAsCuts()]
