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
5. Review the first batch before producing the next batch.

## Safe batch sizes

Recommended:

- Batch A: videos 1 to 3.
- Batch B: videos 4 to 6.
- Batch C: videos 7 to 10.

If render tools are slow, use 2 videos per batch.

## Format standards

- 1080 x 1920 vertical.
- 12 to 20 seconds.
- 3 to 4 slides.
- Large readable text.
- Calm colors.
- No clutter.
- No guaranteed result claims.
- No medical, diagnostic, or official school-testing claims.

## First repair output

The video scripts and upload metadata now live in:

- `video-system/EDUCATION-YOUTUBE-SHORTS-BATCH-01.md`
- `video-system/EDUCATION-YOUTUBE-UPLOAD-METADATA.md`
- `video-system/EDUCATION-CANVA-DESIGN-BRIEF.md`

## Next safe production action

Create the first 3 videos from the scripts:

1. Parent helper tip.
2. Adult learner message.
3. Simple 30-minute routine.

Then review before continuing.
