"""Copy a review SVG without anything taken from the source PDF.

Drops the Source layer (links to the page scans), the hidden Review layer, every <image> and the
<metadata> block, so the copy holds only the traced pieces.
    python3 scripts/strip-svg.py data/bowser/bowser.svg results/bowser/bowser.svg
"""
import sys
import xml.etree.ElementTree as ET

SVG = "http://www.w3.org/2000/svg"
INK = "http://www.inkscape.org/namespaces/inkscape"
DROP_LAYERS = {"Source", "Review"}


class SvgStripper:
    def __init__(self, path: str):
        for prefix, uri in [("", SVG), ("inkscape", INK),
                            ("sodipodi", "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"),
                            ("xlink", "http://www.w3.org/1999/xlink")]:
            ET.register_namespace(prefix, uri)
        self.tree = ET.parse(path)

    def strip(self) -> int:
        dropped = 0
        for parent in self.tree.iter():
            for child in list(parent):
                tag = child.tag.split("}")[-1]
                if tag in ("image", "metadata") or child.get(f"{{{INK}}}label") in DROP_LAYERS:
                    parent.remove(child)
                    dropped += 1
        return dropped

    def write(self, path: str) -> None:
        self.tree.write(path, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    s = SvgStripper(src)
    n = s.strip()
    s.write(dst)
    print(f"{dst}: dropped {n} source/review elements")
