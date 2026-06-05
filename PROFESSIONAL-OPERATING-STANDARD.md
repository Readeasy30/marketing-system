# Professional Operating Standard

Last updated: 2026-06-05

Purpose: Prevent confusion, wrong-account work, duplicated effort, and low-value busywork across Wholelychit projects.

This standard applies before any work on:

- GitHub repositories
- Gmail drafts or sent mail
- marketing campaigns
- website files
- Canva/video/social assets
- outreach lists
- trackers and logs

## Core failure to prevent

Do not act from vague memory.

Before doing work, lock these six items:

```text
Project
Account
Repository
Source of truth
Allowed action
Required log/update
```

If any of these are unclear, inspect available records first. Do not guess.

## The 6-lock gate

### 1. Project lock

Name the exact project.

Examples:

```text
ReadEasy30
MathEasy30
PetNeeds.ai
SlotsFreeUSA
Resturants.ai
BransonBlastUSA
Marketing System
```

Do not mix project drafts, outreach, repos, or campaigns.

### 2. Account lock

Name the exact account or tool being used.

Examples:

```text
Gmail: slotsfreeusa@gmail.com
Gmail: wholelychit@gmail.com
GitHub: Wholelychit/marketing-system
GitHub: Wholelychit/readeasy30.com
GitHub: Wholelychit/matheasy30.com
Cloudflare account
Canva account
```

If the visible account does not match the project, stop and verify.

### 3. Repository lock

Name the exact repository before editing.

Marketing strategy belongs in:

```text
Wholelychit/marketing-system
```

Product website code belongs in its own repo.

Do not put campaign control files inside product repos unless they are small status markers, SEO markers, sitemap/robots updates, or safe website-facing copy files.

### 4. Source-of-truth lock

Find the current controlling file before acting.

For ReadEasy30 + MathEasy30 marketing, open first:

```text
DAILY-EDUCATION-MARKETING-OPERATING-SYSTEM.md
EDUCATION-MAIL-MARKETING-DAILY-RUNBOOK.md
EDUCATION-BATCH-01-POSTING-LOG.md
CAMPAIGN-PUBLISHING-TRACKER.md
```

For daily task routing, open:

```text
CODEX-CURRENT-TASK.md
```

Do not rely only on conversation memory.

### 5. Action lock

State the next action in one sentence before doing it.

Good:

```text
I am checking Gmail for ReadEasy30 + MathEasy30 replies from June 4-5 only.
```

Bad:

```text
I am checking emails.
```

### 6. Log/update lock

Before acting, know where the result must be recorded.

Examples:

```text
EDUCATION-BATCH-01-POSTING-LOG.md
CAMPAIGN-PUBLISHING-TRACKER.md
EDUCATION-MAIL-MARKETING-DAILY-RUNBOOK.md
Daily status note in final answer
```

If an action cannot be logged, it is probably not stable enough to do.

## Email and outreach rule

Never send, draft, or inspect unrelated campaign emails as if they belong to another project.

Before sending any email:

1. Verify project.
2. Verify sender account.
3. Verify recipient.
4. Verify subject.
5. Verify draft body.
6. Verify whether the draft says `do not send`, `portal`, `contact form`, or `manual`.
7. Verify required log destination.

Do not send if:

- no recipient exists
- draft says do not send
- draft is for a portal/contact form
- target project does not match the active project
- the email looks like bulk prospecting
- the user has not clearly asked to send that exact group

## Repository work rule

Before editing a repo:

1. Search for an existing file.
2. Fetch the current file and SHA if updating.
3. Make one complete safe update.
4. Report the commit hash.
5. Do not create duplicates with similar names unless needed.

## Daily marketing rule

For every daily marketing session:

1. Open the current operating file.
2. Read the latest tracker/log.
3. Identify today's one useful action.
4. Complete or block that action.
5. Record what happened.
6. Lock tomorrow's first action.

Do not create more assets until the current batch is posted, blocked, paused, or intentionally moved forward.

## Communication standard

Every report should include only what matters:

```text
What I checked
What I changed
What is blocked
What is next
Commit IDs, if any
```

Do not bury the answer in long explanation.

## Quality standard

Every answer should be:

- specific
- project-aware
- account-aware
- repo-aware
- action-oriented
- honest about uncertainty
- short enough to use
- complete enough to avoid repeating work

## Stop-and-correct triggers

Stop immediately when:

- the wrong project appears
- the wrong Gmail account appears
- the wrong repo appears
- a draft belongs to a different website
- a file says `do not send`
- a platform requires manual login
- a task risks breaking production
- the answer depends on a stale assumption

Then correct the source of truth before continuing.

## Professional default

Do fewer things, but do the right things in the right place.

No guessing. No cross-project mixing. No unlogged work. No pretending a blocker is progress.
