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
when only a JPEG fits under the limit).

Strategy: resize with LANCZOS, try a plain optimized PNG, then palette-quantize
the PNG with fewer and fewer colours until it is under the limit. A banner
(no transparency) falls back to JPEG as a last resort. Prints the final size and
format so the caller can report it. Exits 1 if the limit cannot be met.
"""
import io
import os
import sys

from PIL import Image

LIMIT = 200 * 1000  # strict: under 200 KB whether KB is counted as 1000 or 1024 bytes
ICON_SIZE = 800
BANNER_MAX_W = 1200


def png_bytes(im, colors=None):
    buf = io.BytesIO()
    if colors:
        # FASTOCTREE keeps alpha; MEDIANCUT does not on RGBA.
        im = im.quantize(colors=colors, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE)
    im.save(buf, "PNG", optimize=True)
    return buf.getvalue()


def smallest_png(im):
    data = png_bytes(im)
    if len(data) <= LIMIT:
        return data, "full colour"
    for colors in (256, 192, 128, 96, 64, 48, 32):
        data = png_bytes(im, colors)
        if len(data) <= LIMIT:
            return data, f"{colors} colours"
    return None, None


def jpeg_bytes(im, quality):
    flat = Image.new("RGB", im.size, (250, 249, 245))
    flat.paste(im.convert("RGBA"), mask=im.convert("RGBA").split()[3])
    buf = io.BytesIO()
    flat.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
    return buf.getvalue()


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("icon", "banner", "square"):
        print(__doc__)
        sys.exit(2)
    kind, src = sys.argv[1], sys.argv[2]
    im = Image.open(src).convert("RGBA")

    has_alpha = im.getchannel("A").getextrema()[0] < 255
    if kind == "square":
        w, h = im.size
        if w != h:
            side = min(w, h)
            im = im.crop(((w - side) // 2, (h - side) // 2, (w - side) // 2 + side, (h - side) // 2 + side))
        im = im.resize((ICON_SIZE, ICON_SIZE), Image.LANCZOS)
        base = os.path.splitext(src)[0]
        out = sys.argv[3] if len(sys.argv) > 3 else f"{base}-800.png"
        data, note = (None, None)
        full = png_bytes(im)
        if len(full) <= LIMIT:
            data, note = full, "lossless PNG"
        elif has_alpha:
            data, note = smallest_png(im)
        else:
            for q in range(95, 59, -1):
                d = jpeg_bytes(im, q)
                if len(d) <= LIMIT:
                    data, note = d, f"JPEG quality {q}"
                    out = os.path.splitext(out)[0] + ".jpg"
                    break
        if data is None:
            print(f"FAILED: could not get square under {LIMIT // 1000} KB")
            sys.exit(1)
        with open(out, "wb") as f:
            f.write(data)
        print(f"square: {im.size[0]}x{im.size[1]} px, {len(data) / 1024:.0f} KB, {note} -> {out}")
        return

    if kind == "icon":
        if im.size[0] != im.size[1]:
            side = max(im.size)
            canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
            canvas.paste(im, ((side - im.size[0]) // 2, (side - im.size[1]) // 2))
            im = canvas
        im = im.resize((ICON_SIZE, ICON_SIZE), Image.LANCZOS)
    else:
        w, h = im.size
        if w > BANNER_MAX_W:
            im = im.resize((BANNER_MAX_W, round(h * BANNER_MAX_W / w)), Image.LANCZOS)

    base = os.path.splitext(src)[0]
    default = f"{base}-icon-800.png" if kind == "icon" else f"{base}-banner-1200.png"
    out = sys.argv[3] if len(sys.argv) > 3 else default

    data, note = smallest_png(im)
    if data is None and kind == "banner":
        for q in (92, 88, 84, 80, 75, 70, 65, 60):
            data = jpeg_bytes(im, q)
            if len(data) <= LIMIT:
                note = f"JPEG quality {q}"
                out = os.path.splitext(out)[0] + ".jpg"
                break
        else:
            data = None
    if data is None:
        print(f"FAILED: could not get {kind} under {LIMIT // 1024} KB")
        sys.exit(1)

    with open(out, "wb") as f:
        f.write(data)
    print(f"{kind}: {im.size[0]}x{im.size[1]} px, {len(data) / 1024:.0f} KB, {note} -> {out}")


if __name__ == "__main__":
    main()
