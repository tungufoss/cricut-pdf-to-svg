"""Stage 2b: read the printed edge numbers.

The numbers are about 1.7 mm tall in a 178 dpi JPEG, which is at the edge of what
Tesseract reads reliably. Two readers are combined:

1. Tesseract reads every number, in both upright orientations.
2. Its most confident readings train a nearest-neighbour digit matcher on this
   template's own font, which then reads every number again.

When both agree, or Tesseract is very sure, the reading is accepted. Every edge
number is printed exactly twice, so the remaining labels pick the close candidate
that completes a pair. A label is flagged for review unless it was read
confidently and its number appears exactly twice.
"""

from __future__ import annotations

import collections
import itertools
import math
import os
import shutil
from concurrent.futures import ThreadPoolExecutor

import cv2
import numpy as np

from .model import Label

HEIGHT = 24        # px, upright number height used for matching
CELL_WIDTH = 14    # px, normalised digit width
TRUST = 93.0       # Tesseract confidence accepted on its own
TRAIN = 90.0       # Tesseract confidence good enough to learn a digit from


def read_paper(footer: np.ndarray | None) -> str:
    """Read the cardstock colour from the page's "Print on ... paper" margin note."""
    if footer is None or shutil.which("tesseract") is None:
        return ""
    import re
    import pytesseract

    gray = cv2.cvtColor(footer, cv2.COLOR_RGB2GRAY)
    image = cv2.resize(cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE), None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    image = np.where(image < 200, 0, 255).astype(np.uint8)
    text = pytesseract.image_to_string(image, config="--psm 6")
    match = re.search(r"print\s+on\s+(\w+)\s+paper", text, re.IGNORECASE)
    return match.group(1).lower() if match else ""


def _upright(ink: np.ndarray, angle: float) -> np.ndarray | None:
    """Rotate a white-on-black number crop upright and scale it to HEIGHT px."""
    big = cv2.resize(ink, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    side = int(math.hypot(*big.shape)) + 8
    canvas = np.zeros((side, side), np.uint8)
    oy, ox = (side - big.shape[0]) // 2, (side - big.shape[1]) // 2
    canvas[oy:oy + big.shape[0], ox:ox + big.shape[1]] = big
    turned = cv2.warpAffine(canvas, cv2.getRotationMatrix2D((side / 2, side / 2), angle, 1), (side, side),
                            flags=cv2.INTER_CUBIC)
    ys, xs = np.nonzero(turned > 100)
    if not len(xs):
        return None
    crop = turned[ys.min():ys.max() + 1, xs.min():xs.max() + 1].astype(np.float32)
    width = max(1, round(crop.shape[1] * HEIGHT / crop.shape[0]))
    return cv2.resize(crop, (width, HEIGHT), interpolation=cv2.INTER_AREA) / 255.0


def _split(image: np.ndarray, digits: int) -> list[np.ndarray] | None:
    """Cut an upright number into digit cells at the faintest columns near even spacing."""
    width = image.shape[1]
    if digits == 1:
        return [image]
    profile = image.sum(axis=0)
    cuts = [0]
    for k in range(1, digits):
        expected = k * width / digits
        lo = max(int(expected - 0.35 * width / digits), cuts[-1] + 1)
        hi = min(int(expected + 0.35 * width / digits) + 1, width - 1)
        if hi <= lo:
            return None
        cuts.append(lo + int(np.argmin(profile[lo:hi])))
    cuts.append(width)
    cells = [image[:, a:b] for a, b in zip(cuts, cuts[1:])]
    return cells if all(cell.shape[1] >= 2 for cell in cells) else None


def _feature(cell: np.ndarray) -> np.ndarray:
    columns = np.nonzero(cell.max(axis=0) > 0.4)[0]
    if len(columns):
        cell = cell[:, columns.min():columns.max() + 1]
    vector = cv2.resize(cell, (CELL_WIDTH, HEIGHT), interpolation=cv2.INTER_AREA).ravel()
    vector = vector - vector.mean()
    norm = np.linalg.norm(vector)
    return vector / norm if norm else vector


class EdgeNumberReader:
    def __init__(self, workers: int | None = None):
        self.workers = workers or os.cpu_count() or 1
        self.available = shutil.which("tesseract") is not None
        self.templates = np.zeros((0, HEIGHT * CELL_WIDTH))
        self.digits = np.zeros(0, dtype="<U1")

    def read_all(self, labels: list[Label]) -> None:
        """Fill in text, orientation and confidence on every label, in place."""
        if not labels:
            return
        if not self.available:
            for label in labels:
                label.text, label.confident = "?", False
            return
        os.environ.setdefault("OMP_THREAD_LIMIT", "1")  # one thread per Tesseract process
        with ThreadPoolExecutor(self.workers) as pool:
            tesseract = list(pool.map(self._tesseract, labels))
        self._train(labels, tesseract)
        candidates = [self._candidates(label) for label in labels]
        decided: list[int] = []
        for i, (label, (t_text, t_conf, t_flip), options) in enumerate(zip(labels, tesseract, candidates)):
            if t_text and ((options and t_text == options[0][0]) or t_conf >= TRUST):
                label.text, label.confident = t_text, True
                label.angle = (label.angle + t_flip) % 360
                decided.append(i)
        self._pair_up(labels, candidates, [t for t, _, _ in tesseract], decided)

    @staticmethod
    def _pair_up(labels: list[Label], candidates, tesseract: list[str], decided: list[int]) -> None:
        """Every edge number is printed exactly twice, once on each edge that is glued
        together. Uncertain labels prefer a close candidate that completes a pair, and
        any number that does not end up printed exactly twice is flagged."""
        counts = collections.Counter(labels[i].text for i in decided)
        settled = set(decided)
        undecided = [i for i in range(len(labels)) if i not in settled]
        undecided.sort(key=lambda i: -(candidates[i][0][1] if candidates[i] else -math.inf))
        for i in undecided:
            options = candidates[i]
            if not options:
                labels[i].text, labels[i].confident = "?", False
                continue
            best = options[0][1]
            close = [o for o in options if o[1] >= best - 0.05]
            pick = (next((o for o in close if counts[o[0]] == 1), None)
                    or next((o for o in close if counts[o[0]] == 0), None)
                    or options[0])
            # Completing a pair with a reading one of the two readers ranked first is good evidence.
            completes = counts[pick[0]] == 1 and (pick is options[0] or pick[0] == tesseract[i])
            labels[i].text, labels[i].confident = pick[0], completes
            labels[i].angle = (labels[i].angle + pick[2]) % 360
            counts[pick[0]] += 1
        for label in labels:
            label.paired = counts[label.text] == 2

    def _tesseract(self, label: Label) -> tuple[str, float, int]:
        import pytesseract

        best = ("", -1.0, 0)
        for flip in (0, 180):
            image = _upright(label.ink, label.angle + flip)
            if image is None:
                continue
            page = cv2.resize((255 - np.pad(image, 10) * 255).astype(np.uint8), None, fx=2, fy=2)
            data = pytesseract.image_to_data(page, config="--psm 7 -c tessedit_char_whitelist=0123456789",
                                             output_type=pytesseract.Output.DICT)
            words = [(text, float(conf)) for text, conf in zip(data["text"], data["conf"]) if text.strip()]
            if words:
                text, conf = "".join(w for w, _ in words), min(c for _, c in words)
                if conf > best[1]:
                    best = (text, conf, flip)
        return best

    def _train(self, labels: list[Label], tesseract) -> None:
        samples: dict[str, list[np.ndarray]] = collections.defaultdict(list)
        for label, (text, conf, flip) in zip(labels, tesseract):
            if conf < TRAIN or not 2 <= len(text) <= 3:
                continue
            image = _upright(label.ink, label.angle + flip)
            cells = _split(image, len(text)) if image is not None else None
            for digit, cell in zip(text, cells or []):
                samples[digit].append(_feature(cell))
        pairs = [(digit, vector) for digit, vectors in sorted(samples.items()) for vector in vectors]
        if pairs:
            self.digits = np.array([d for d, _ in pairs])
            self.templates = np.array([v for _, v in pairs])

    def _candidates(self, label: Label, keep: int = 8) -> list[tuple[str, float, int]]:
        """Most likely readings as (text, score, flip), best first."""
        if not len(self.templates):
            return []
        classes = sorted(set(self.digits))
        found: dict[tuple[str, int], float] = {}
        for flip in (0, 180):
            image = _upright(label.ink, label.angle + flip)
            if image is None:
                continue
            for count in (1, 2, 3):
                cells = _split(image, count)
                if not cells:
                    continue
                # Digits are roughly 0.3-1.0 times as wide as they are tall.
                penalty = 0.0 if 0.3 < image.shape[1] / HEIGHT / count < 1.0 else 0.3
                options = []
                for cell in cells:
                    similarity = self.templates @ _feature(cell)
                    per_digit = {d: float(np.sort(similarity[self.digits == d])[-3:].mean()) for d in classes}
                    options.append(sorted(per_digit.items(), key=lambda item: -item[1])[:2])
                for combo in itertools.product(*options):
                    text = "".join(d for d, _ in combo)
                    score = sum(v for _, v in combo) / count - penalty
                    if score > found.get((text, flip), -math.inf):
                        found[(text, flip)] = score
        ranked = sorted(((t, sc, f) for (t, f), sc in found.items()), key=lambda item: -item[1])
        return ranked[:keep]
