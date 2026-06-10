#!/usr/bin/env python3
"""
make_shorts.py
--------------
Turns a folder of images (Canva exports, screenshots, worksheet pics) into a
ready-to-upload vertical short video (1080 x 1920) for YouTube Shorts, Reels,
and TikTok. Optionally adds a caption on each image and background music.

WHAT IT DOES
  - Reads every image in the INPUT_FOLDER (in name order)
  - Fits each one onto a 1080x1920 vertical frame
  - Draws an optional caption (from the CAPTIONS list below)
  - Plays each image for SECONDS_PER_IMAGE
  - Adds optional background music
  - Saves one .mp4 you can upload anywhere

ONE-TIME SETUP (run these two lines in a terminal):
  pip install moviepy pillow
  # moviepy installs ffmpeg automatically the first time it runs.

HOW TO USE
  1. Put your images in a folder (e.g. a folder named "clips" next to this file).
  2. Edit the SETTINGS block below (folder name, caption text, music file).
  3. Run:  python make_shorts.py
  4. Your video appears as the OUTPUT_FILE name below.

Brand feel for education videos: calm, helpful, simple, confidence-building.
"""

import os
import sys
import glob
import tempfile

# ============================ SETTINGS ============================
INPUT_FOLDER      = "clips"            # folder of images to turn into a short
OUTPUT_FILE       = "short.mp4"        # name of the video this creates
SECONDS_PER_IMAGE = 3.0                # how long each image stays on screen
FADE_SECONDS      = 0.4               # gentle fade between images
MUSIC_FILE        = ""                 # e.g. "music.mp3"  (leave "" for none)
MUSIC_VOLUME      = 0.35               # 0.0 = silent, 1.0 = full volume

# One caption per image, in the same order as the files. Leave "" for no text.
# Extra images with no caption listed here simply show no text.
CAPTIONS = [
    # "Free reading help, 30 days.",
    # "Practice a little every day.",
    # "readeasy30.com",
]

# Look of the caption
FONT_SIZE     = 64
TEXT_COLOR    = (255, 255, 255)        # white
BAR_COLOR     = (31, 56, 100)          # navy bar behind the text
BAR_OPACITY   = 200                    # 0-255
CANVAS_BG     = (20, 24, 33)           # background behind images that don't fill
FPS           = 30
# ==================================================================

W, H = 1080, 1920

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Pillow is not installed. Run:  pip install pillow")

try:
    from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip, afx
except ImportError:
    sys.exit("moviepy is not installed. Run:  pip install moviepy")


def load_font(size):
    """Use a common system font; fall back to Pillow's default if not found."""
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "arialbd.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def wrap(draw, text, font, max_width):
    words, lines, line = text.split(), [], ""
    for w in words:
        test = (line + " " + w).strip()
        if draw.textlength(test, font=font) <= max_width:
            line = test
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def build_frame(img_path, caption):
    """Fit one image onto a vertical canvas and draw an optional caption."""
    canvas = Image.new("RGB", (W, H), CANVAS_BG)
    photo = Image.open(img_path).convert("RGB")
    scale = min(W / photo.width, H / photo.height)
    new = (max(1, int(photo.width * scale)), max(1, int(photo.height * scale)))
    photo = photo.resize(new, Image.LANCZOS)
    canvas.paste(photo, ((W - new[0]) // 2, (H - new[1]) // 2))

    if caption:
        draw = ImageDraw.Draw(canvas, "RGBA")
        font = load_font(FONT_SIZE)
        lines = wrap(draw, caption, font, W - 160)
        line_h = FONT_SIZE + 18
        block_h = line_h * len(lines)
        top = H - block_h - 200            # sit caption near the lower third
        draw.rectangle(
            [0, top - 40, W, top + block_h + 40],
            fill=(BAR_COLOR[0], BAR_COLOR[1], BAR_COLOR[2], BAR_OPACITY),
        )
        y = top
        for ln in lines:
            tw = draw.textlength(ln, font=font)
            draw.text(((W - tw) / 2, y), ln, font=font, fill=TEXT_COLOR)
            y += line_h

    return canvas


def main():
    if not os.path.isdir(INPUT_FOLDER):
        sys.exit(f'Folder "{INPUT_FOLDER}" not found. '
                 f'Create it and put your images inside, then run again.')

    exts = ("*.png", "*.jpg", "*.jpeg", "*.webp", "*.PNG", "*.JPG", "*.JPEG")
    files = sorted(f for e in exts for f in glob.glob(os.path.join(INPUT_FOLDER, e)))
    if not files:
        sys.exit(f'No images found in "{INPUT_FOLDER}".')

    print(f"Found {len(files)} image(s). Building {OUTPUT_FILE} ...")
    tmpdir = tempfile.mkdtemp()
    clips = []
    for i, path in enumerate(files):
        caption = CAPTIONS[i] if i < len(CAPTIONS) else ""
        frame_path = os.path.join(tmpdir, f"frame_{i:03d}.png")
        build_frame(path, caption).save(frame_path)
        clip = ImageClip(frame_path).set_duration(SECONDS_PER_IMAGE)
        if FADE_SECONDS > 0:
            clip = clip.crossfadein(FADE_SECONDS)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose", padding=-FADE_SECONDS)

    if MUSIC_FILE:
        if os.path.isfile(MUSIC_FILE):
            audio = AudioFileClip(MUSIC_FILE).volumex(MUSIC_VOLUME)
            audio = afx.audio_loop(audio, duration=video.duration)
            video = video.set_audio(audio)
        else:
            print(f'(Skipping music — "{MUSIC_FILE}" not found.)')

    video.write_videofile(OUTPUT_FILE, fps=FPS, codec="libx264",
                          audio_codec="aac", preset="medium")
    print(f"\nDone. Your short is: {OUTPUT_FILE}")
    print("Upload it to YouTube Shorts, Reels, or TikTok.")


if __name__ == "__main__":
    main()
