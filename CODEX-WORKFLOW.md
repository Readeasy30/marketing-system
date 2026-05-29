# CODEX-WORKFLOW.md

Last updated: 2026-05-29

## Purpose

Codex is the main workflow for routine GitHub repository editing across Wholelychit projects.

The goal is simple: Gerry should not waste time manually pasting, creating, replacing, repairing, or updating repo files when Codex can safely do that work directly.

## Operating workflow

Use ChatGPT 5.5 and Codex as the production workflow.

No local Git. No terminal Git. No VS Code requirement. No manual file creation or paste updates.

Workflow:

1. ChatGPT 5.5 manages the plan.
2. Codex performs repository work.
3. GitHub stores files and commits.
4. Cloudflare Pages publishes from GitHub when connected.

## Why Codex is used

Codex is better for multi-file repository work because it can:

- read the repository first
- understand the current file structure
- keep the existing tech stack
- create safe new files
- update existing files
- repair broken files
- commit useful changes
- continue through a safe queue without stopping after one tiny task

## Use ChatGPT GitHub connector for

- small direct file updates
- repo checks
- status verification
- emergency fixes
- when Codex is awkward or blocked

Internal write-action labels like `create_file` or `update_file` mean the AI is requesting permission to create or update a file. They are not instructions for Gerry to manually create files.

## Primary rule

Do not ask Gerry to paste, create, replace, or update repo files manually.

When write access is available, Codex or the GitHub connector should create, update, replace, repair, and commit safe files directly.

## Required work pattern

1. Read the repo first.
2. Check `README.md`.
3. Check `AGENTS.md`.
4. Check `CODEX-WORKFLOW.md`.
5. Check `CODEX-CURRENT-TASK.md` if present.
6. Check `PROJECT-STATUS.md` if present.
7. Check any locked checkpoint or file-management notes if present.
8. Keep the current tech stack.
9. Do not migrate frameworks.
10. Do not delete major working code.
11. Make safe edits directly.
12. Commit each useful group of changes.
13. Continue through the safe queue until blocked.
14. Report only after useful commits or a real blocker.

## Real blockers only

Stop only for:

- missing repo permission
- account sign-in problem
- credentials or private keys
- billing or payment setup
- live ads
- live tracking scripts
- framework migration
- major code deletion
- unclear production risk that cannot be safely repaired

## Safe work allowed

Codex may directly handle:

- Markdown documentation updates
- README updates
- AGENTS.md updates
- CODEX-WORKFLOW.md updates
- CODEX-CURRENT-TASK.md updates
- PROJECT-STATUS.md updates
- CHANGELOG.md updates
- robots.txt updates
- sitemap.xml updates
- SEO checklist updates
- launch checklist updates
- content planning files
- campaign files
- simple HTML updates
- simple CSS updates
- simple JavaScript repairs
- broken link fixes
- footer/navigation cleanup
- accessibility improvements
- mobile layout improvements
- safe copy improvements
- safe scripts and templates
- non-secret configuration examples

## Work not allowed without direct approval

Do not proceed without direct approval for:

- private keys
- API tokens
- payment processing
- checkout setup
- billing setup
- live ad network scripts
- live tracking scripts
- affiliate links
- public AI tools
- upload systems
- user accounts
- ordering integrations
- deleting major working code
- changing the site framework
- switching to React, Vite, Next.js, TypeScript, or build tools unless the repo already uses them and the project checkpoint allows it

## If blocked

Record the blocker in `PROJECT-STATUS.md` if possible.

Move to the next safe task or next repository. Do not ask Gerry to do manual file work.

## Future Wholelychit starter repo recommendation

Future repos should start from a simple template that already includes:

- `README.md`
- `AGENTS.md`
- `CODEX-WORKFLOW.md`
- `CODEX-CURRENT-TASK.md`
- `PROJECT-STATUS.md`
- `CHANGELOG.md`
- `robots.txt`
- `sitemap.xml`
- `SEO-CHECKLIST.md`
- `LAUNCH-CHECKLIST.md`
- `REVIEW-CHECKLIST.md`
- basic `/css` and `/js` folders when the site is static
- clear deployment notes

This avoids repeating setup work and keeps every repo ready for Codex-first production edits.

## Final operating rule

Codex should keep moving through safe repo work without making Gerry babysit routine file changes.

Record blockers. Commit safe progress. Report only when useful work is complete or a real blocker appears.
