# Email Sender Setup Checklist

Last updated: 2026-06-04

Campaign: **ReadEasy30 + MathEasy30**

Sender / reply email:

```text
free@readeasy30.com
```

## Current decision

Use Mailjet later for provider sending.

Use Gmail/manual contact forms until sender setup is complete.

## Setup order

1. Confirm `free@readeasy30.com` exists.
2. Confirm the inbox receives mail.
3. Confirm the address can send mail.
4. Create or open Mailjet account.
5. Add `free@readeasy30.com` as a sender.
6. Verify the sender/domain in Mailjet.
7. Add the DNS records Mailjet provides.
8. Send one internal test email.
9. Send one manual public-contact test.
10. Review bounce/reply handling.
11. Begin warm-up from the quota calendar.

## Do not store in this repo

Do not store passwords.
Do not store API keys.
Do not store SMTP keys.
Do not store recovery codes.
Do not store private DNS tokens.

## Required before provider sending

- `EMAIL-SUPPRESSION-LIST.csv` exists.
- `OUTREACH-DAILY-240-TRACKER.csv` exists.
- Templates include `free@readeasy30.com`.
- Every contact is verified as public and relevant.
- Opt-outs are honored.

## First safe test

Send one message to your own mailbox first.

Then send one verified public contact-form message.

Do not jump directly to 200/day until the sender is verified and replies/bounces are being tracked.
