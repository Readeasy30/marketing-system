# Professional Operating Standard

Last updated: 2026-06-05

Purpose: Prevent confusion, wrong-account work, duplicated effort, stale assumptions, fake progress, and low-value busywork across Wholelychit projects.

This standard applies before any work on:

- GitHub repositories
- Gmail drafts or sent mail
- marketing campaigns
- website files
- Canva/video/social assets
- outreach lists
- trackers and logs
- email platform setup

## Core failure to prevent

Do not act from vague memory.

Do not answer from confidence.

Answer from the current source of truth.

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

## Current ReadEasy30 + MathEasy30 campaign fact lock

These facts are locked until Gerry directly changes them:

| Field | Locked value |
|---|---|
| Active campaign | ReadEasy30 + MathEasy30 education outreach |
| Daily outreach target | 180 good-fit contacts per day |
| Segment structure | 6 groups x 30 contacts |
| Sender | `free@readeasy30.com` |
| Reply-to | `free@readeasy30.com` |
| Backup owner email | `wholelychit@gmail.com` |
| Primary recovered list | `readeasy30_matheasy30_daily_outreach_mail_list_180.xlsx` |
| Recovery workbook | `readeasy30_matheasy30_NO_STOP_OUTREACH_EXECUTION.xlsx` |
| Recovered index | `RECOVERED-OUTREACH-CONTACTS-INDEX-2026-06-05.md` |
| Email setup file | `EDUCATION-EMAIL-SENDER-SETUP-2026-06-05.md` |
| Daily run sheet | `EDUCATION-180-DAILY-SEND-RUN-SHEET-2026-06-05.md` |

Never replace `free@readeasy30.com` with `wholelychit@gmail.com` in campaign setup unless Gerry explicitly says it is a temporary backup.

## Current outreach count lock

Do not confuse rows with sends.

| Term | Meaning |
|---|---|
| Row built | A possible contact exists in the recovered list |
| Ready row | Contact route appears usable, but still needs execution |
| Send | A public direct email was actually sent or approved platform sent it |
| Submit | A public contact/resource form was manually completed |
| Blocked | Tool, login, safety, platform, or page rule prevents execution |
| Complete | Real send/submit/post occurred and was logged |

Do not report a send unless a send actually happened.

Do not report completion if the work is only planned, drafted, organized, or queued.

## The 6-lock gate

### 1. Project lock

Name the exact project.

Examples:

```text
ReadEasy30
MathEasy30
PetNeeds.ai
SlotsFreeUSA
restaurantaibot.com
BransonBlastUSA
Marketing System
```

Do not mix project drafts, outreach, repos, or campaigns.

### 2. Account lock

Name the exact account or tool being used.

Examples:

```text
Sender: free@readeasy30.com
Backup Gmail: wholelychit@gmail.com
GitHub: Wholelychit/marketing-system
GitHub: Wholelychit/readeasy30.com
GitHub: Wholelychit/matheasy30.com
Cloudflare account
Canva account
Brevo account
```

If the visible account does not match the project, stop and verify.

### 3. Repository lock

Name the exact repository before editing.

Marketing strategy belongs in:

```text
Wholelychit/marketing-system
```

Product website code belongs in its own repo.

Do not put campaign control files inside product repos unless they are small status markers, SEO markers, sitemap/robots updates, QA files, or safe website-facing copy files.

### 4. Source-of-truth lock

Find the current controlling file before acting.

For ReadEasy30 + MathEasy30 outreach, open first:

```text
RECOVERED-OUTREACH-CONTACTS-INDEX-2026-06-05.md
EDUCATION-EMAIL-SENDER-SETUP-2026-06-05.md
EDUCATION-180-DAILY-SEND-RUN-SHEET-2026-06-05.md
CAMPAIGN-PUBLISHING-TRACKER.md
```

For ReadEasy30 + MathEasy30 marketing status, open first:

```text
PROJECT-STATUS.md
EDUCATION-MARKETING-TABLE-ACTION-BOARD-2026-06-04.md
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
I am checking the recovered outreach index and sender setup before changing the email plan.
```

Bad:

```text
I am checking emails.
```

### 6. Log/update lock

Before acting, know where the result must be recorded.

Examples:

```text
PROJECT-STATUS.md
CAMPAIGN-PUBLISHING-TRACKER.md
EDUCATION-180-DAILY-SEND-RUN-SHEET-2026-06-05.md
EDUCATION-EMAIL-SENDER-SETUP-2026-06-05.md
Daily status note in final answer
```

If an action cannot be logged, it is probably not stable enough to do.

## Email and outreach rule

Never send, draft, or inspect unrelated campaign emails as if they belong to another project.

Before sending or setting up any email campaign:

1. Verify project.
2. Verify sender account.
3. Verify sending platform.
4. Verify recipient list source.
5. Verify recipient count.
6. Verify subject.
7. Verify draft body.
8. Verify opt-out handling.
9. Verify whether the route says `do not send`, `portal`, `contact form`, `manual`, or `direct email`.
10. Verify required log destination.

Do not send if:

- no recipient exists
- sender is not verified
- draft says do not send
- target project does not match the active project
- the email looks like unmanaged bulk prospecting
- required sender, opt-out, or address setup is missing
- user has not clearly approved that exact platform/list/send action

## Required correction behavior

When Gerry says “check your notes,” do this before answering:

1. Stop.
2. Search or fetch the relevant source-of-truth files.
3. Quote the locked fact in plain English.
4. Correct the prior answer.
5. Update the repo if the incorrect fact was written anywhere.
6. Report the commit ID if changed.

Do not argue from memory.

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
- source-of-truth-aware
- action-oriented
- honest about uncertainty
- short enough to use
- complete enough to avoid repeating work

## Stop-and-correct triggers

Stop immediately when:

- the wrong project appears
- the wrong sender appears
- the wrong Gmail account appears
- the wrong repo appears
- a draft belongs to a different website
- a file says `do not send`
- a platform requires manual login
- a task risks breaking production
- the answer depends on a stale assumption
- a send count is being confused with a row count
- Gerry says the answer conflicts with prior notes

Then correct the source of truth before continuing.

## Professional default

Do fewer things, but do the right things in the right place.

No guessing. No cross-project mixing. No unlogged work. No pretending a blocker is progress. No replacing locked facts from memory.
