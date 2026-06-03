# Education Batch 01 Deep-Link Metadata QA

Last updated: 2026-06-03

Campaign: **ReadEasy30 + MathEasy30 — 30 Minutes. One Calm Step.**

## Scope lock

Only covers:

```text
ReadEasy30 + MathEasy30 Batch 01
```

Do not use this file for SlotsFreeUSA or any other project.

## Purpose

Record metadata checks for the deep-link pages used by Batch 01 posts, pins, and captions.

## Completed

### Adult learner page

Repo file:

```text
Wholelychit/readeasy30.com/adult-reading-practice-without-shame.html
```

Status:

```text
Completed
```

Completed updates:

- Open Graph metadata added.
- Twitter summary metadata added.
- Existing title confirmed.
- Existing meta description confirmed.
- Existing robots metadata confirmed.
- Existing canonical URL confirmed.
- Existing theme color confirmed.

Purpose:

This supports the adult learner / no-shame Batch 01 post.

## Checked but not changed

### Reading worksheet hub

Repo file:

```text
Wholelychit/readeasy30.com/printable-reading-worksheets.html
```

Status:

```text
Checked only
```

Reason:

The page is longer than the connector returned as one complete safe file. To avoid a risky partial overwrite, no update was made from this chat.

Existing metadata confirmed:

- title
- meta description
- robots
- theme color
- canonical URL

Future safe action:

Use Codex or a patch-capable editor to add Open Graph and Twitter summary metadata only.

### Math worksheet hub

Repo file:

```text
Wholelychit/matheasy30.com/printable-math-worksheets.html
```

Status:

```text
Blocked
```

Reason:

The safe metadata update attempt was blocked by OpenAI safety checks during the GitHub write.

Existing metadata confirmed:

- title
- meta description
- canonical URL

Future safe action:

Use Codex or a patch-capable editor to add:

```text
robots meta
theme-color meta
Open Graph metadata
Twitter summary metadata
```

## Already completed homepage metadata work

Recorded in:

```text
EDUCATION-BATCH-01-WEBSITE-METADATA-QA.md
```

Completed pages:

```text
Wholelychit/readeasy30.com/index.html
Wholelychit/matheasy30.com/index.html
```

## Current campaign stop point

Content, assets, copy, and major landing-page metadata are ready.

The true active blocker remains manual social posting access.

## Next single action

Post Card 1 manually using:

```text
01-readeasy30-matheasy30-card-1-calm-step.png
EDUCATION-BATCH-01-FIRST-POST-CLIPBOARD.md
```

Then paste the live post link back into ChatGPT.