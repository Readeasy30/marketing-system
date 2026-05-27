# File Management Rules

## Purpose

Keep Wholelychit repositories clean, simple, and easy for AI/Codex to improve without repeating work.

## Main rule

AI and Codex do file work directly.

Do not ask Gerry to paste, create, or update files manually.

## Before creating a file

1. Check whether the file already exists.
2. Check whether a similar file already exists under a different name.
3. Prefer improving an existing file over creating a duplicate.
4. Create a new file only when it makes the system clearer.

## Before editing a website repo

Read these files when present:

1. `README.md`
2. `AGENTS.md`
3. `AGENT-INSTRUCTIONS.md`
4. `LOCKED-CHECKPOINT.md`
5. `FILE-MANAGEMENT.md`
6. `PROJECT-STATUS.md`

## Safe file update rules

- Use full-file replacement when small patches are fragile.
- Use small focused edits when the file is stable and the change is simple.
- Keep file names clear and boring.
- Avoid duplicate CSS files.
- Avoid duplicate JavaScript files.
- Avoid repeated planning files with nearly the same purpose.
- Do not delete major files unless references are checked first.
- Do not move files unless links/imports are checked first.
- Commit each useful safe change.

## Repository boundaries

`marketing-system` holds planning and systems.

Website repositories hold live site code.

Do not put another site's homepage, CSS, app code, or deployment files in `marketing-system`.

## Standard command-center files

Use these names when possible:

- `REPOSITORY-MASTER-MAP.md`
- `CODEX-PRODUCTION-WORKFLOW.md`
- `FILE-MANAGEMENT.md`
- `TIME-MANAGEMENT.md`
- `WEBSITE-PRIORITY-LIST.md`
- `PROMPT-LIBRARY.md`
- `CROSS-SITE-LAUNCH-CHECKLIST.md`
- `REVIEW-FIX-LOOP.md`
- `LEGAL-PAGE-INSTRUCTIONS.md`

## Standard website repo files

Use these names when possible:

- `README.md`
- `AGENTS.md`
- `AGENT-INSTRUCTIONS.md`
- `LOCKED-CHECKPOINT.md`
- `PROJECT-STATUS.md`
- `FILE-MANAGEMENT.md`
- `SEO-CHECKLIST.md`
- `LAUNCH-CHECKLIST.md`
- `CONTENT-PLAN.md`
- `STYLE-GUIDE.md`
- `DEPLOYMENT-NOTES.md`

## Blocker log rule

When a task is blocked, write down:

1. What was blocked.
2. Why it was blocked.
3. What file or setting caused it.
4. What the next safe action is.

Then continue with another safe item.

## Never add

- private keys
- API tokens
- payment credentials
- live ad scripts
- live analytics/tracking scripts without approval
- secret URLs
- personal data
- unsupported claims
