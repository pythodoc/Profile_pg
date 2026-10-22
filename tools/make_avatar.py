"""Compose the circular avatar used in the hero.

The source headshot is cropped tight at the crown, so a straight square crop
puts the hair on the edge of the circular mask. We extend the studio backdrop
upward (seamlessly, since it is a soft dark vignette), then crop with real
headroom and the eye line at ~40% — the classic portrait composition.

Outputs:
  profile/assets/profile.png        square, unmasked (CSS draws the circle)
  shots/avatar-circle-preview.png   masked proof at the real on-page sizes
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / "shots" / "live-desktop.png"
OUT_SQUARE = BASE / "profile" / "assets" / "profile.png"
OUT_PREVIEW = BASE / "shots" / "avatar-circle-preview.png"

# photo area inside the old card, excluding its 1px border
PHOTO_BOX = (398, 158, 838, 800)

PAD_TOP = 80
SIDE = 380
HEADROOM = 0.09  # crown distance from the top of the square, as a fraction
FEATHER = 10  # rows over which the synthetic backdrop blends into the photo


def _backdrop_row(photo: Image.Image) -> list[tuple[int, int, int]]:
    """Top backdrop row with the hair replaced by the corner-to-corner falloff.

    Using the real row keeps the studio glow, so the seam is invisible; the hair
    pixels would otherwise smear a dark block above the crown.
    """
    w = photo.width
    top = photo.crop((0, 0, w, 6)).resize((w, 1), Image.BOX)
    row = list(top.getdata())

    left = tuple(sum(c[i] for c in row[:40]) // 40 for i in range(3))
    right = tuple(sum(c[i] for c in row[-40:]) // 40 for i in range(3))

    repaired: list[tuple[int, int, int]] = []
    for x, px in enumerate(row):
        t = x / max(1, w - 1)
        base = tuple(int(left[i] + (right[i] - left[i]) * t) for i in range(3))
        dist = sum(abs(px[i] - base[i]) for i in range(3))
        repaired.append(px if dist <= 18 else base)  # type: ignore[arg-type]

    # soften any residual steps
    out = []
    for x in range(w):
        lo, hi = max(0, x - 12), min(w, x + 13)
        win = repaired[lo:hi]
        out.append(tuple(sum(c[i] for c in win) // len(win) for i in range(3)))  # type: ignore[misc]
    return out  # type: ignore[return-value]


def build() -> Image.Image:
    src = Image.open(SRC).convert("RGB")
    photo = src.crop(PHOTO_BOX)
    row = _backdrop_row(photo)

    # 1. synthetic backdrop above the crown, following the vignette upward
    pad = Image.new("RGB", (photo.width, PAD_TOP))
    for y in range(PAD_TOP):
        t = y / max(1, PAD_TOP - 1)  # 0 at top, 1 at the seam
        factor = 0.9 + 0.1 * t
        colour = [tuple(min(255, int(c * factor)) for c in px) for px in row]
        line = Image.new("RGB", (photo.width, 1))
        line.putdata(colour)
        pad.paste(line, (0, y))

    canvas = Image.new("RGB", (photo.width, photo.height + PAD_TOP))
    canvas.paste(pad, (0, 0))

    # feather the join so no hard line survives
    alpha = Image.new("L", photo.size, 255)
    for y in range(FEATHER):
        alpha.paste(int(255 * (y / FEATHER)), (0, y, photo.width, y + 1))
    canvas.paste(photo, (0, PAD_TOP), alpha)

    # 2. crop so the crown lands at HEADROOM and the face is horizontally centred
    face_cx = 200
    hair_top = PAD_TOP + 10
    y0 = int(round(hair_top - HEADROOM * SIDE))
    x0 = int(round(face_cx - SIDE / 2))
    square = canvas.crop((x0, y0, x0 + SIDE, y0 + SIDE))
    return square.resize((520, 520), Image.LANCZOS)


def preview(square: Image.Image) -> None:
    """Render the mask + ring exactly as the page draws it, at both sizes."""
    bg = (7, 11, 20)
    sizes = [186, 118]
    gap = 56
    width = sum(sizes) + gap * (len(sizes) + 1)
    height = max(sizes) + gap * 2
    out = Image.new("RGB", (width, height), bg)

    x = gap
    for size in sizes:
        big = square.resize((size * 3, size * 3), Image.LANCZOS)  # supersample
        mask = Image.new("L", big.size, 0)
        ImageDraw.Draw(mask).ellipse((0, 0, big.width - 1, big.height - 1), fill=255)
        big = big.resize((size, size), Image.LANCZOS)
        mask = mask.resize((size, size), Image.LANCZOS)
        out.paste(big, (x, gap), mask)
        # 1px ring + 6px outer glow, matching box-shadow in main.css
        d = ImageDraw.Draw(out)
        d.ellipse((x, gap, x + size - 1, gap + size - 1), outline=(78, 90, 110), width=1)
        d.ellipse((x - 3, gap - 3, x + size + 2, gap + size + 2), outline=(30, 38, 52), width=2)
        x += size + gap

    out.save(OUT_PREVIEW)


if __name__ == "__main__":
    avatar = build()
    OUT_SQUARE.parent.mkdir(parents=True, exist_ok=True)
    avatar.save(OUT_SQUARE, optimize=True)
    preview(avatar)
    print("square:", avatar.size, OUT_SQUARE.stat().st_size, "bytes")
    print("preview:", OUT_PREVIEW)
