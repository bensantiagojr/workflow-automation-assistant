#!/usr/bin/env python3
"""Resize ChatGPT email images to the email specs.

  icon    -> 800x800 px PNG, transparency kept, under 200 KB
  banner  -> max width 1200 px (aspect ratio kept), under 200 KB
  square  -> 800x800 px, under 200 KB, best format picked automatically:
             PNG if the image has transparency or a lossless PNG fits,
             otherwise JPEG at the highest quality that fits (photos, headshots).
             Non-square input is centre-cropped to a square.

Usage:
  python3 -I resize_email_images.py icon   INPUT [OUTPUT]
  python3 -I resize_email_images.py banner INPUT [OUTPUT]
  python3 -I resize_email_images.py square INPUT [OUTPUT]

INPUT can be png, webp or jpg. If OUTPUT is omitted it is written next to the
input as <name>-icon-800.png, <name>-banner-1200.png or <name>-800.png (or .jpg
when a JPEG is the best fit under the limit).

Strategy (quality first, smallest change that fits):
  * Image WITH transparency (icon): lossless PNG if it fits, then full-colour PNG
    with the colour depth and the soft-shadow alpha reduced step by step (smooth,
    no banding), and only then a 256-colour palette PNG as a last resort.
  * Image WITHOUT transparency (banner, photos): lossless PNG if it fits, then a
    high-quality JPEG (quality 95 down to 70), and only then a palette PNG.
Prints the final size and method. Exits 1 if the limit cannot be met.
"""
import io
import os
import sys

from PIL import Image

LIMIT = 200 * 1000  # strict: under 200 KB whether KB is counted as 1000 or 1024 bytes
ICON_SIZE = 800
BANNER_MAX_W = 1200

# (colour bits per channel, alpha bits, alpha cut-off) tried in order, best quality first
REDUCTIONS = [(6, 5, 24), (5, 5, 24), (5, 4, 24), (5, 3, 24), (4, 3, 24)]


def png_bytes(im, colors=None):
    buf = io.BytesIO()
    if colors:
        # FASTOCTREE is the only quantizer that keeps alpha on RGBA.
        im = im.quantize(colors=colors, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE)
    im.save(buf, "PNG", optimize=True)
    return buf.getvalue()


def _lut(bits):
    top = (1 << bits) - 1
    return [((v >> (8 - bits)) * 255) // top for v in range(256)]


def reduced_rgba(im, bits, abits, cut):
    """Reduce colour depth and alpha levels; fully transparent pixels become black."""
    r, g, b, a = im.convert("RGBA").split()
    lut = _lut(bits)
    alut = _lut(abits)
    a = a.point([0 if v < cut else alut[v] for v in range(256)])
    r, g, b = r.point(lut), g.point(lut), b.point(lut)
    clear = a.point([255 if v == 0 else 0 for v in range(256)])
    black = Image.new("L", im.size, 0)
    for band in (r, g, b):
        band.paste(black, mask=clear)
    return Image.merge("RGBA", (r, g, b, a))


def transparent_png(im):
    """Best-quality PNG under the limit for an image with transparency."""
    data = png_bytes(im)
    if len(data) <= LIMIT:
        return data, "lossless PNG"
    for bits, abits, cut in REDUCTIONS:
        data = png_bytes(reduced_rgba(im, bits, abits, cut))
        if len(data) <= LIMIT:
            return data, f"full-colour PNG, {bits}-bit colour / {abits}-bit alpha"
    for colors in (256, 192, 128, 96, 64):
        data = png_bytes(im, colors)
        if len(data) <= LIMIT:
            return data, f"{colors}-colour palette PNG"
    return None, None


def jpeg_bytes(im, quality):
    flat = Image.new("RGB", im.size, (250, 249, 245))
    rgba = im.convert("RGBA")
    flat.paste(rgba, mask=rgba.split()[3])
    buf = io.BytesIO()
    flat.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
    return buf.getvalue()


def opaque_best(im, out):
    """Best format under the limit for an image with no transparency."""
    data = png_bytes(im)
    if len(data) <= LIMIT:
        return data, "lossless PNG", out
    for q in range(95, 69, -1):
        d = jpeg_bytes(im, q)
        if len(d) <= LIMIT:
            return d, f"JPEG quality {q}", os.path.splitext(out)[0] + ".jpg"
    for colors in (256, 192, 128, 96, 64):
        d = png_bytes(im, colors)
        if len(d) <= LIMIT:
            return d, f"{colors}-colour palette PNG", out
    return None, None, out


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("icon", "banner", "square"):
        print(__doc__)
        sys.exit(2)
    kind, src = sys.argv[1], sys.argv[2]
    im = Image.open(src).convert("RGBA")
    has_alpha = im.getchannel("A").getextrema()[0] < 255
    base = os.path.splitext(src)[0]

    if kind in ("icon", "square"):
        w, h = im.size
        if w != h:
            if kind == "square":
                side = min(w, h)
                left, top = (w - side) // 2, (h - side) // 2
                im = im.crop((left, top, left + side, top + side))
            else:
                side = max(w, h)
                canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
                canvas.paste(im, ((side - w) // 2, (side - h) // 2))
                im = canvas
        im = im.resize((ICON_SIZE, ICON_SIZE), Image.LANCZOS)
        out = sys.argv[3] if len(sys.argv) > 3 else (
            f"{base}-icon-800.png" if kind == "icon" else f"{base}-800.png")
        if has_alpha or kind == "icon":
            data, note = transparent_png(im)
        else:
            data, note, out = opaque_best(im, out)
    else:
        w, h = im.size
        if w > BANNER_MAX_W:
            im = im.resize((BANNER_MAX_W, round(h * BANNER_MAX_W / w)), Image.LANCZOS)
        out = sys.argv[3] if len(sys.argv) > 3 else f"{base}-banner-1200.png"
        if has_alpha:
            data, note = transparent_png(im)
        else:
            data, note, out = opaque_best(im, out)

    if data is None:
        print(f"FAILED: could not get {kind} under {LIMIT // 1000} KB")
        sys.exit(1)
    with open(out, "wb") as f:
        f.write(data)
    print(f"{kind}: {im.size[0]}x{im.size[1]} px, {len(data) / 1024:.0f} KB, {note} -> {out}")


if __name__ == "__main__":
    main()
