# Project Status

Last updated: 2026-06-02

This file tracks the safe marketing-system queue for Wholelychit projects.

## Current Workflow Decision

Codex is the primary workflow for routine repository edits.

The ChatGPT GitHub connector is secondary and should be used only for small reads, checks, reviews, or emergency single-file edits when Codex is unavailable.

## Active Portfolio Plan

The current locked marketing direction is the Wholelychit multi-site portfolio plan.

Sites covered:

1. SlotsFreeUSA
2. RestaurantAIbot / Resturants.ai
3. ReadEasy30
4. MathEasy30
5. PetNeeds.ai
6. BransonBlastUSA

## Current Marketing Execution Layer Added

Decision locked:

- Marketing-system should not only hold plans. It should also hold reusable weekly execution boards, campaign assets, and publishing trackers.
- Website code stays in each website repo.
- Marketing repo stores strategy, captions, scripts, Canva prompts, campaign tracking, outreach rules, and review-control files.

New marketing execution files:

- `PORTFOLIO-WEEKLY-EXECUTION-BOARD.md`
- `RESTURANTS-AI-OWNER-RESOURCE-CAMPAIGN.md`
- `CAMPAIGN-PUBLISHING-TRACKER.md`
- `CHANGELOG.md`

## RestaurantAIbot Campaign Status

Current focus:

RestaurantAIbot / Resturants.ai owner-resource promotion.

Website repo already has owner resource pages. Marketing-system now has matching campaign assets:

- social captions
- short video scripts
- Canva prompts
- email/newsletter draft
- campaign CTA direction
- manual success metrics

Next useful actions:

1. Create first 3 Canva graphics from `RESTURANTS-AI-OWNER-RESOURCE-CAMPAIGN.md`.
2. Turn the first 3 captions into publish-ready platform posts.
3. Create a simple one-page Restaurant Growth Starter Checkup PDF later if requested.
4. Add a reusable `PUBLISHING-QUEUE.md` if campaign volume grows.

## Education Outreach Repair Added

Decision locked:

- ReadEasy30 and MathEasy30 outreach must use organized prospect standards.
- Direct emails, contact forms, directories, media-only contacts, and blocked contacts must be separated.
- Do not mass-send.
- Do not scrape private emails.
- Use official public contact routes only.
- One follow-up only after 7 to 10 days.
- Stop on opt-out or no-contact requests.

New education outreach files:

- `OUTREACH/README.md`
- `OUTREACH/EDUCATION-PROSPECT-QUEUE.md`
- `OUTREACH/CONTACT-FORM-SCRIPTS.md`
- `OUTREACH/GMAIL-SEND-BLOCK-LOG.md`
- `OUTREACH/DAILY-EXECUTION-RULES.md`
- `OUTREACH/EMAIL-READY-CONTACT-STANDARDS.md`

## Education Video Repair Added

Decision locked:

- Do not render 10 YouTube Shorts MP4 files in one long run.
- Use script/metadata/Canva-first workflow.
- Create videos in smaller batches of 2 to 3 videos.
- Keep videos vertical, short, readable, and calm.

New education video files:

- `video-system/EDUCATION-YOUTUBE-SHORTS-BATCH-01.md`
- `video-system/EDUCATION-YOUTUBE-UPLOAD-METADATA.md`
- `video-system/EDUCATION-CANVA-DESIGN-BRIEF.md`
- `video-system/VIDEO-GENERATION-REPAIR-NOTES.md`

## Avatar and Video System Added

Decision locked:

- Marketing repo stores reusable avatar and video systems.
- Each website repo stores final site-specific avatar personality, final dialogue, placement plan, and embed notes.
- Large final videos should usually be hosted outside GitHub through an approved video platform.

Existing reusable files:

- `avatar-system/README.md`
- `avatar-system/AVATAR-WORKFLOW.md`
- `avatar-system/AVATAR-PERSONALITY-TEMPLATE.md`
- `avatar-system/AVATAR-DIALOGUE-LIBRARY.md`
- `avatar-system/AVATAR-EMBED-TEMPLATE.md`
- `video-system/README.md`
- `video-system/SHORT-VIDEO-SCRIPT-TEMPLATE.md`
- `video-system/CANVA-VIDEO-CHECKLIST.md`
- `prompt-library/AVATAR-PROMPT.md`
- `prompt-library/VIDEO-SCRIPT-PROMPT.md`

## BransonBlastUSA Note

Repo identified as `Wholelychit/bransonblastusa.com`.

Misspelled `branssonblastusa.com` repo was not found.

BransonBlastUSA should use the shared avatar/video system from this repo, then store final site-specific avatar files in its own repo.

## Current Safe Queue

1. Use `PORTFOLIO-WEEKLY-EXECUTION-BOARD.md` to pick one weekly focus.
2. Use `RESTURANTS-AI-OWNER-RESOURCE-CAMPAIGN.md` to create the first RestaurantAIbot Canva/social batch.
3. Track published assets in `CAMPAIGN-PUBLISHING-TRACKER.md`.
4. Continue ReadEasy30 + MathEasy30 outreach using `OUTREACH/DAILY-EXECUTION-RULES.md`.
5. Produce the first 3 education short videos from `video-system/EDUCATION-YOUTUBE-SHORTS-BATCH-01.md`.
6. Continue BransonBlastUSA static repo repair later: `script.js`, `robots.txt`, `sitemap.xml`, status files, and CSS completion if needed.
7. Record blockers instead of stopping.

## Current Blockers

- One outreach email to the national Head Start contact route was sent on 2026-06-02.
- Gmail blocked direct send/draft attempts to two public library contact routes; use official contact forms/manual one-to-one route instead of repeated Gmail attempts.
- The initial 10-video ffmpeg batch timed out; use script/metadata/Canva-first workflow and produce MP4s in smaller batches.
- `slotsfreeusa@mail.com` requires Gerry to click the Cloudflare verification link in the mail.com inbox.
- Gmail “Send as” for `@slotsfreeusa.com` requires Gmail settings and an outbound SMTP provider; Cloudflare Email Routing is inbound forwarding only.
- One active avatar embed HTML template write was blocked by connector safety checks; a safe markdown planning template was created instead.
- Manual browser QA is still required after public deployment.

## Notes

Build practical systems Gerry can reuse across multiple websites. Keep language direct, simple, and action-based.
