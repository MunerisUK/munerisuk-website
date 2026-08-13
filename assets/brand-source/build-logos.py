#!/usr/bin/env python3
"""Regenerate the site's logo assets from the original Muneris artwork.

The files alongside this script are the source art as supplied. They carry a
solid white or #EEF2F5 ground and a lot of surrounding space, so they are not
usable on a web page directly. This trims each to its content, knocks the
ground out to transparency and writes web-sized PNGs into assets/img/.

    pip install Pillow
    python3 assets/brand-source/build-logos.py

Run this rather than hand-editing anything in assets/img/.
"""

from pathlib import Path
from PIL import Image, ImageChops

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "img"

WHITE = (255, 255, 255)
TINT = (238, 242, 245)          # #EEF2F5, the brand's light ground
SLATE = (87, 110, 126)          # #576E7E, the wordmark colour


def trim(im: Image.Image, ground: tuple) -> Image.Image:
    """Crop away the uniform ground surrounding the artwork."""
    rgb = im.convert("RGB")
    bbox = ImageChops.difference(rgb, Image.new("RGB", rgb.size, ground)).getbbox()
    return im.crop(bbox)


def knock_out(im: Image.Image, ground: tuple, tol: int) -> Image.Image:
    """Make the ground transparent, leaving antialiased edges intact."""
    im = im.convert("RGBA")
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if all(abs(c - k) <= tol for c, k in zip((r, g, b), ground)):
                px[x, y] = (r, g, b, 0)
    return im


def recolour_slate_to_white(im: Image.Image, tol: int = 40) -> Image.Image:
    """Reverse treatment: slate becomes white, cyan and orange are untouched."""
    im = im.copy()
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a > 0 and all(abs(c - k) < tol for c, k in zip((r, g, b), SLATE)):
                px[x, y] = (255, 255, 255, a)
    return im


def save(im: Image.Image, name: str, width: int) -> None:
    height = round(width * im.height / im.width)
    im.resize((width, height), Image.LANCZOS).save(OUT / name, optimize=True)
    print(f"{name:38} {width}x{height}")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    # Horizontal lockup — wordmark left, symbol right, on white.
    horiz = knock_out(trim(Image.open(HERE / "muneris logo horizontal.png"), WHITE),
                      WHITE, tol=10)
    save(horiz, "muneris-logo-horizontal.png", 600)
    save(recolour_slate_to_white(horiz), "muneris-logo-horizontal-reverse.png", 600)

    # Stacked lockup — symbol above wordmark, on the brand tint.
    stacked = trim(Image.open(HERE / "muneris_plain_lightgray_1920x1080.png"), TINT)
    save(knock_out(stacked, TINT, tol=14), "muneris-logo-stacked.png", 360)

    # Symbol alone, taken from the top of the stacked lockup.
    mark = stacked.crop((0, 0, stacked.width, 330))
    mark = trim(mark, TINT)
    save(knock_out(mark, TINT, tol=14), "muneris-symbol.png", 256)


if __name__ == "__main__":
    main()
