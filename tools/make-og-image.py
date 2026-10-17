#!/usr/bin/env python3
"""Generate a 1200x630 OG image for Godot Engine docs (docs.godotengine.org).

Pillow-only, byte-reproducible. Clean card matching the Godot brand:
dark navy ground (#293252), #478cbf blue accent, #ff4e78 pink accent,
Godot wordmark + tagline, section pills + domain chip.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
NAVY = (41, 50, 82)          # #293252 Godot dark navy
BLUE = (71, 140, 191)        # #478cbf Godot blue
PINK = (255, 78, 120)        # #ff4e78 Godot pink accent
WHITE = (255, 255, 255)
LIGHT = (214, 222, 235)      # light text on navy
GREY = (150, 160, 180)
NAVY2 = (30, 37, 62)         # darker navy for chips

FONT_DIR = os.environ.get("FONT_DIR", "/usr/share/fonts/truetype/dejavu")


def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    p = os.path.join(FONT_DIR, name)
    if not os.path.exists(p):
        p = os.path.join(FONT_DIR, "LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf")
    return ImageFont.truetype(p, size)


def rounded(d, box, r, fill):
    d.rounded_rectangle(box, radius=r, fill=fill)


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # top accent bar (Godot blue)
    d.rectangle([0, 0, W, 10], fill=BLUE)

    f_title = font(88, bold=True)
    f_sub = font(34)
    f_pill = font(30, bold=True)
    f_domain = font(30, bold=True)
    f_foot = font(24)

    # title + subtitle
    d.text((70, 60), "Godot Engine", font=f_title, fill=WHITE)
    d.text((70, 196), "Free and open source 2D and 3D game engine.", font=f_sub, fill=LIGHT)
    d.text((70, 240), "Official documentation.", font=f_sub, fill=LIGHT)

    # separator
    d.line([70, 320, W - 70, 320], fill=(70, 82, 120), width=2)

    # section pills
    pills = ["Getting started", "Step-by-step", "Tutorials", "Class reference", "Community"]
    x = 70
    y = 356
    for p_ in pills:
        w = d.textlength(p_, font=f_pill) + 44
        if x + w > 1130:
            x = 70
            y += 82
        rounded(d, [x, y, x + w, y + 62], 31, BLUE)
        d.text((x + 22, y + 13), p_, font=f_pill, fill=WHITE)
        x += w + 18

    # footer domain chip
    d.rounded_rectangle([70, H - 92, 470, H - 44], 24, fill=NAVY2)
    d.text((108, H - 84), "docs.godotengine.org", font=f_domain, fill=WHITE)

    # subtle Godot "G" motif top-right (ring + node dot)
    cx, cy = W - 200, 150
    d.ellipse([cx - 60, cy - 60, cx + 60, cy + 60], outline=PINK, width=8)
    d.ellipse([cx - 18, cy - 18, cx + 18, cy + 18], fill=PINK)

    out = "og-image.png"
    img.save(out, "PNG")
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
