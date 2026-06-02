# Video Generation Repair Notes

Last updated: 2026-06-02

## Problem

The local YouTube Shorts batch generation attempted to render 10 MP4 files in one run using ffmpeg. The process timed out before completion.

## Repair decision

Do not try to render all 10 MP4 files in one run.

Use this safer production order:

1. Create scripts.
2. Create upload metadata.
3. Create Canva design brief.
4. Produce videos in smaller batches of 2 to 3.
5. Review each completed batch before continuing.

## Safe batch sizes

Recommended:

- Batch A: videos 1 to 3.
- Batch B: videos 4 to 6.
- Batch C: videos 7 to 10.

If render tools are slow, use 2 videos per batch.

## Format standards

- Vertical short-video format.
- 12 to 20 seconds.
- 3 to 4 slides.
- Large readable text.
- Calm colors.
- No clutter.
- No guaranteed result claims.
- No medical, diagnostic, or official school-testing claims.

## First repair output

The video scripts and upload metadata live in:

- `video-system/EDUCATION-YOUTUBE-SHORTS-BATCH-01.md`
- `video-system/EDUCATION-YOUTUBE-UPLOAD-METADATA.md`
- `video-system/EDUCATION-CANVA-DESIGN-BRIEF.md`

## Batch A completed

Batch A rendered successfully in ChatGPT sandbox on 2026-06-02.

Files produced:

1. `01-parent-helper-tip.mp4`
2. `02-adult-learner-message.mp4`
3. `03-30-minute-routine.mp4`

Also produced:

- matching thumbnail PNG files
- upload metadata CSV
- upload instruction README
- batch preview PNG
- downloadable ZIP package

Download package created in sandbox:

`/mnt/data/readeasy30_matheasy30_youtube_shorts_BATCH_A.zip`

## Next safe production action

Create Batch B:

1. Progress, not perfect.
2. Calm helper reminder.
3. For readers who freeze.

Use the same smaller-batch render method that succeeded for Batch A.
