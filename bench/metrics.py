"""Conventional and fabrication-aware metrics for one predicted page.

Conventional (visual) metrics compare the rendered prediction with the raster the method
was given, which is what image vectorization optimizes: raster IoU, mean (chamfer) and
Hausdorff distance between ink, and vector complexity.

Fabrication metrics compare the prediction with the vector ground truth (paper 1, F1-F6):

F1 closed    share of pieces cut by a closed contour that matches the piece (IoU >= CLOSED_IOU)
F2 dim       error of matched pieces' box sides, in mm and relative
F3 cut/fold  precision, recall and F1 per class at TOL_MM
F4 topology  duplicate contours per piece, extra contours, cut paths per piece outline,
             fragments per fold, folds missing
F5 match     length difference between the two copies of each glued edge
F6 complex   paths, nodes, control points, SVG bytes

Every function returns flat {metric: value} dicts so results land in one tidy CSV.
"""

from __future__ import annotations

import math

import cv2
import numpy as np
from scipy.spatial import cKDTree
from shapely.geometry import Polygon
from shapely.strtree import STRtree

from .baselines import ink
from .model import CUT, FOLD, Page, Prediction

TOL_MM = 0.5            # how far a predicted line may sit from the true one
STEP_MM = 0.25          # sampling step along lines
SNAP_MM = 1.0           # how far a predicted vertex may sit from a true edge end
MIN_AREA = 4.0          # mm^2, smaller closed paths are not candidate pieces
CLOSED_IOU = 0.8        # loose on purpose: position and scale errors belong to F2, not F1


def sample(polylines, closed_flags=None, step=STEP_MM) -> np.ndarray:
    """Points every `step` mm along polylines."""
    out = []
    for i, pts in enumerate(polylines):
        pts = list(pts)
        if closed_flags is not None and closed_flags[i]:
            pts = pts + pts[:1]
        for a, b in zip(pts, pts[1:]):
            a, b = np.asarray(a, float), np.asarray(b, float)
            n = max(1, int(np.linalg.norm(b - a) / step))
            out.append(a + (b - a) * np.linspace(0, 1, n, endpoint=False)[:, None])
        if pts:
            out.append(np.asarray(pts[-1:], float))
    return np.vstack(out) if out else np.zeros((0, 2))


def _near(points: np.ndarray, tree: cKDTree | None, tol=TOL_MM) -> np.ndarray:
    if tree is None or len(points) == 0:
        return np.zeros(len(points), bool)
    d, _ = tree.query(points, distance_upper_bound=tol)
    return np.isfinite(d)


def _tree(points: np.ndarray) -> cKDTree | None:
    return cKDTree(points) if len(points) else None


class Evaluator:
    def __init__(self, truth: Page, gray: np.ndarray, dpi: int):
        self.truth, self.gray, self.dpi = truth, gray, dpi
        self.px = dpi / 25.4
        self.pieces = [Polygon(p.outline, p.holes) for p in truth.pieces]
        self.gt_cut = sample(truth.cut_paths())
        self.gt_fold = sample(truth.fold_paths())
        self.fold_samples = [sample([f]) for f in truth.fold_paths()]
        self.outline_samples = [sample([p.outline], [True]) for p in truth.pieces]

    def evaluate(self, pred: Prediction, raw: Prediction | None = None) -> dict[str, float]:
        """`raw` is the method's own output before the shared classifier split its paths;
        visual and complexity metrics judge that, fabrication metrics the classified one."""
        raw = raw or pred
        out = {}
        out.update(self.visual(raw))
        out.update(self.complexity(raw))
        out.update(self.closure_and_dims(pred))
        out.update(self.semantics(pred))
        out.update(self.topology(pred))
        out.update(self.matching(pred))
        return out

    # ---- conventional ------------------------------------------------------------
    def render(self, pred: Prediction) -> np.ndarray:
        h, w = self.gray.shape
        canvas = np.zeros((h, w), np.uint8)
        if pred.filled:
            # Outlines nest (a stroke is the ring between its outer and inner contour), so
            # fill even-odd: each polygon flips the pixels it covers.
            for p in pred.paths:
                if len(p.points) < 3:
                    continue
                pts = np.round(np.asarray(p.points) * self.px).astype(np.int32)
                x0, y0 = np.maximum(pts.min(axis=0), 0)
                x1, y1 = np.minimum(pts.max(axis=0) + 1, (w, h))
                if x1 <= x0 or y1 <= y0:
                    continue
                tile = np.zeros((y1 - y0, x1 - x0), np.uint8)
                cv2.fillPoly(tile, [pts - (x0, y0)], 255)
                canvas[y0:y1, x0:x1] ^= tile
        else:
            width = max(1, round(self.stroke_px()))
            for p in pred.paths:
                pts = np.round(np.asarray(p.points) * self.px * 16).astype(np.int32)
                cv2.polylines(canvas, [pts], p.closed, 255, width, lineType=cv2.LINE_8, shift=4)
        return canvas > 0

    def stroke_px(self) -> float:
        mask = ink(self.gray).astype(np.uint8)
        dist = cv2.distanceTransform(mask, cv2.DIST_L2, 3)
        ridge = dist[(dist > 0) & (dist >= cv2.dilate(dist, np.ones((3, 3), np.uint8)))]
        return 2 * float(np.median(ridge)) if len(ridge) else 1.0

    def visual(self, pred: Prediction) -> dict[str, float]:
        source = ink(self.gray)
        drawn = self.render(pred)
        union = (source | drawn).sum()
        iou = float((source & drawn).sum() / union) if union else 1.0
        to_source = cv2.distanceTransform((~source).astype(np.uint8), cv2.DIST_L2, 3)
        to_drawn = cv2.distanceTransform((~drawn).astype(np.uint8), cv2.DIST_L2, 3)
        a, b = to_source[drawn], to_drawn[source]
        mm = 1 / self.px
        both = np.concatenate([a, b]) if len(a) and len(b) else np.array([np.inf])
        return {"raster_iou": iou,
                "chamfer_mm": float(both.mean() * mm),
                "hausdorff_mm": float(both.max() * mm),
                "hausdorff95_mm": float(np.percentile(both, 95) * mm)}

    @staticmethod
    def complexity(pred: Prediction) -> dict[str, float]:
        nodes = sum(len(p.points) for p in pred.paths)
        controls = sum(p.controls or len(p.points) for p in pred.paths)
        return {"paths": len(pred.paths), "nodes": nodes, "controls": controls, "svg_bytes": pred.svg_bytes}

    # ---- fabrication ---------------------------------------------------------------
    def _closed_cuts(self, pred: Prediction) -> list[Polygon]:
        polys = []
        for p in pred.paths:
            if p.closed and p.kind == CUT and len(p.points) >= 3:
                poly = Polygon(p.points).buffer(0)
                if poly.area >= MIN_AREA:
                    polys.append(poly)
        return polys

    def _piece_matches(self, pred: Prediction):
        polys = self._closed_cuts(pred)
        tree = STRtree(polys) if polys else None
        best, dupes = [], []
        matched = set()
        for gt in self.pieces:
            ious = []
            if tree is not None:
                for i in tree.query(gt):
                    inter = gt.intersection(polys[i]).area
                    if inter:
                        iou = inter / gt.union(polys[i]).area
                        ious.append((iou, int(i)))
            ious.sort(reverse=True)
            best.append((ious[0][0], polys[ious[0][1]]) if ious else (0.0, None))
            dupes.append(sum(1 for iou, _ in ious if iou >= 0.9))
            matched.update(i for iou, i in ious if iou >= 0.5)
        extra = len(polys) - len(matched)
        return best, dupes, extra

    @staticmethod
    def _box_sides(poly: Polygon) -> list[float]:
        xs, ys = poly.minimum_rotated_rectangle.exterior.coords.xy
        return sorted([math.dist((xs[0], ys[0]), (xs[1], ys[1])), math.dist((xs[1], ys[1]), (xs[2], ys[2]))])

    def closure_and_dims(self, pred: Prediction) -> dict[str, float]:
        best, dupes, extra = self._piece_matches(pred)
        closed = sum(1 for iou, _ in best if iou >= CLOSED_IOU)
        errs, rels = [], []
        for gt, (iou, poly) in zip(self.pieces, best):
            if iou >= 0.5:
                g, p = self._box_sides(gt), self._box_sides(poly)
                for gs, ps in zip(g, p):
                    errs.append(abs(ps - gs))
                    rels.append(abs(ps - gs) / gs)
        n = len(self.pieces)
        return {"F1_closed": closed / n,
                "F2_dim_mm": float(np.mean(errs)) if errs else math.nan,
                "F2_dim_rel": float(np.mean(rels)) if rels else math.nan,
                "F4_duplicate_contours": float(np.mean([max(0, d - 1) for d in dupes])),
                "F4_extra_contours": extra / n}

    def semantics(self, pred: Prediction) -> dict[str, float]:
        out = {}
        f1s = []
        for kind, gt in ((CUT, self.gt_cut), (FOLD, self.gt_fold)):
            paths = [p for p in pred.paths if p.kind == kind]
            ps = sample([p.points for p in paths], [p.closed for p in paths])
            precision = float(_near(ps, _tree(gt)).mean()) if len(ps) else 0.0
            recall = float(_near(gt, _tree(ps)).mean()) if len(gt) else 1.0
            f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
            out.update({f"F3_{kind}_precision": precision, f"F3_{kind}_recall": recall, f"F3_{kind}_f1": f1})
            f1s.append(f1)
        out["F3_macro_f1"] = float(np.mean(f1s))
        return out

    def topology(self, pred: Prediction) -> dict[str, float]:
        def assign(paths, targets):
            counts = np.zeros(len(targets), int)
            trees = [_tree(t) for t in targets]
            for p in paths:
                s = sample([p.points], [p.closed])
                if not len(s):
                    continue
                shares = [float(_near(s, t).mean()) for t in trees]
                k = int(np.argmax(shares)) if shares else -1
                if k >= 0 and shares[k] >= 0.5:
                    counts[k] += 1
            return counts
        cut_counts = assign([p for p in pred.paths if p.kind == CUT], self.outline_samples)
        fold_counts = assign([p for p in pred.paths if p.kind == FOLD], self.fold_samples)
        covered = fold_counts[fold_counts > 0]
        return {"F4_cut_paths_per_piece": float(cut_counts.mean()),
                "F4_fragments_per_fold": float(covered.mean()) if len(covered) else math.nan,
                "F4_folds_missing": float((fold_counts == 0).mean()) if len(fold_counts) else 0.0}

    def matching(self, pred: Prediction) -> dict[str, float]:
        vertices = np.array([q for p in pred.paths for q in p.points], float).reshape(-1, 2)
        tree = _tree(vertices)
        edges = {e.id: e for piece in self.truth.pieces for e in piece.edges}

        def measured(e):
            if tree is None:
                return None
            d, i = tree.query([e.a, e.b], distance_upper_bound=SNAP_MM)
            if not np.all(np.isfinite(d)):
                return None
            return float(np.linalg.norm(vertices[i[0]] - vertices[i[1]]))

        diffs, length_errs, missing, pairs = [], [], 0, 0
        for e in edges.values():
            if not e.matches or e.id > e.matches or e.matches not in edges:
                continue
            pairs += 1
            li, lj = measured(e), measured(edges[e.matches])
            if li is None or lj is None:
                missing += 1
                continue
            diffs.append(abs(li - lj))
            length_errs += [abs(li - e.length), abs(lj - edges[e.matches].length)]
        return {"F5_match_diff_mm": float(np.mean(diffs)) if diffs else math.nan,
                "F5_match_over_0.5mm": float(np.mean(np.array(diffs) > 0.5)) if diffs else math.nan,
                "F5_edge_length_err_mm": float(np.mean(length_errs)) if length_errs else math.nan,
                "F5_pairs_unmeasurable": missing / pairs if pairs else math.nan}
