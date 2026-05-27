# Terminal Execution Runbook

Use these commands to run the local media workflow.

## 1. Open the correct folder

Replace the example path with the real location on your computer.

### Windows Command Prompt

```bat
cd C:\path\to\your\slotsfreeusa_media_vault
```

### Mac or Linux Terminal

```bash
cd /path/to/your/slotsfreeusa_media_vault
```

## 2. Verify core files are present

You should see these files or folders:

- `video_scripts.json`
- `generate_scripts.py`
- `rename_assets.bat`
- `01_raw_renders`
- `02_voiceovers`
- `03_production_ready`

### Windows

```bat
dir
```

### Mac or Linux

```bash
ls
```

## 3. Generate compiled script files

Run this from the same folder as `generate_scripts.py` and `video_scripts.json`.

### Windows

```bat
python generate_scripts.py
```

If `python` does not work, try:

```bat
py generate_scripts.py
```

### Mac or Linux

```bash
python3 generate_scripts.py
```

## 4. Generate a custom number of scripts

### Windows

```bat
python generate_scripts.py --count 10
```

### Mac or Linux

```bash
python3 generate_scripts.py --count 10
```

## 5. Check output folder

The script creates this folder:

```txt
compiled_scripts
```

Open it and confirm the compiled `.txt` script files were created.

### Windows

```bat
dir compiled_scripts
```

### Mac or Linux

```bash
ls compiled_scripts
```

## 6. Prepare production-ready assets

Move finished `.mp4` and matching `.mp3` files into:

```txt
03_production_ready
```

Then copy `rename_assets.bat` into the same folder.

## 7. Rename finished media files

### Windows

Open `03_production_ready`, then double-click:

```txt
rename_assets.bat
```

Or run it from Command Prompt:

```bat
cd 03_production_ready
rename_assets.bat
```

## 8. Final check before posting

Confirm:

- File names are clean.
- Video and audio match.
- Captions are readable.
- Required age/terms text is visible.
- Final files are in the correct topic folder.
