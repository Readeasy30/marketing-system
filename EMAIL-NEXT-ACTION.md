# Email Next Action

Last updated: 2026-06-04

Campaign: ReadEasy30 + MathEasy30

Campaign email:

```text
free@readeasy30.com
```

## Open first

```text
TODAY-MARKETING-ACTION.md
EMAIL-30-DAY-QUOTA-PLAN.md
EMAIL-30-DAY-QUOTA-CALENDAR.csv
EMAIL-SENDER-SETUP-CHECKLIST.md
MAILJET-SETUP-RUNBOOK.md
MAILJET-CLOUDFLARE-DNS-CHECKLIST.md
```

## Current state

The 30-day quota system is built.

The next work is setup and verification of the campaign email.

## Exact next actions

### Step 1 — Test mailbox

1. Send a test message to `free@readeasy30.com`.
2. Confirm it arrives.
3. Send a reply from `free@readeasy30.com` to Gerry.
4. Confirm the reply arrives.

### Step 2 — Start Mailjet

1. Open Mailjet.
2. Create or sign in to the account.
3. Add sender email: `free@readeasy30.com`.
4. Add domain: `readeasy30.com`.
5. Copy the exact DNS records Mailjet shows.

### Step 3 — Add DNS in Cloudflare

1. Open Cloudflare.
2. Choose `readeasy30.com`.
3. Open DNS records.
4. Add the Mailjet records exactly as shown.
5. Do not delete existing website records.
6. Return to Mailjet and click verify/check.

### Step 4 — Test sending

1. Send one internal test email.
2. Send one verified public contact-form message.
3. Log the result.
4. Start the quota calendar only after test sending works.

## Do not redo

Do not rebuild the plan tomorrow.
Do not create a second email plan.
Do not change the daily target unless the campaign changes.

## Daily target after setup

```text
200 provider emails + 40 manual or contact-form actions = 240 outreach actions per day
```

## Stop if blocked

If any step is blocked, record the exact blocker and continue with manual contact-form preparation only.
