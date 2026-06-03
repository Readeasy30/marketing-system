# Education Batch 01 Live Link QA

Last updated: 2026-06-03

Campaign: **ReadEasy30 + MathEasy30 — 30 Minutes. One Calm Step.**

Purpose: Confirm Batch 01 destination links before posting.

## QA method

Direct live-domain browser opening was not available from the current tool session.

Fallback QA used GitHub repo files as the source of truth. If Cloudflare Pages is synced to the default branches, these URLs are safe to use. If a live link fails during manual posting, use the homepage backup and record the blocker.

## ReadEasy30 destination files

| URL | Repo file | Status | Use in Batch 01 |
|---|---|---|---|
| `https://readeasy30.com/` | `Wholelychit/readeasy30.com/index.html` | File exists | Main reading link |
| `https://readeasy30.com/app.html` | `Wholelychit/readeasy30.com/app.html` | File exists | App/deep practice link |
| `https://readeasy30.com/printable-reading-worksheets.html` | `Wholelychit/readeasy30.com/printable-reading-worksheets.html` | File exists | Reading worksheet pin |
| `https://readeasy30.com/adult-reading-practice-without-shame.html` | `Wholelychit/readeasy30.com/adult-reading-practice-without-shame.html` | File exists | Adult learner pin/post |

## MathEasy30 destination files

| URL | Repo file | Status | Use in Batch 01 |
|---|---|---|---|
| `https://matheasy30.com/` | `Wholelychit/matheasy30.com/index.html` | File exists | Main math link |
| `https://matheasy30.com/app.html` | `Wholelychit/matheasy30.com/app.html` | File exists | App/deep practice link |
| `https://matheasy30.com/printable-math-worksheets.html` | `Wholelychit/matheasy30.com/printable-math-worksheets.html` | File exists | Math worksheet pin |

## Approved links for Batch 01 copy

Use these in posts:

```text
https://readeasy30.com/
https://matheasy30.com/
https://readeasy30.com/app.html
https://matheasy30.com/app.html
https://readeasy30.com/printable-reading-worksheets.html
https://matheasy30.com/printable-math-worksheets.html
https://readeasy30.com/adult-reading-practice-without-shame.html
```

## Backup rule

If a deep link fails during manual posting, use the homepage instead:

```text
https://readeasy30.com/
https://matheasy30.com/
```

Then record the failed link in:

- `EDUCATION-BATCH-01-POSTING-LOG.md`
- `CAMPAIGN-PUBLISHING-TRACKER.md`

## Result

Batch 01 link QA is ready from repo-file verification.

Manual live browser QA is still recommended immediately before posting.