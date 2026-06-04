# Outreach Email Tool Decision

Last updated: 2026-06-04

Campaign: **ReadEasy30 + MathEasy30**

## Decision

Use this stack now:

1. GitHub repository files for the operating system, source map, templates, and logs.
2. Google Sheets or CSV tracker for contact management.
3. Gmail/manual contact forms for first outreach messages.
4. Mailjet later when we have verified, compliant contacts and need higher-volume sending.

## Do not use yet

Do not connect Mailjet, Resend, Mailgun, SendPulse, or any SMTP/API sender today.

Reason:

- We need verified public contacts first.
- We need opt-out and suppression tracking first.
- We need list hygiene before using an email provider.
- We must avoid bulk unsolicited sending.

## Provider decision notes

### Mailjet

Best future fit for this plan because the free tier supports up to 200 emails per day and includes SMTP/API features.

Use later after list hygiene and opt-out tracking are stable.

### Resend

Good developer tool for transactional email and clean API work, but the free daily limit is lower than the 240/day outreach target.

Do not use for this outreach engine first.

### Mailgun

Good developer tool for transactional delivery, but its free plan is also below the 240/day outreach target.

Do not use first.

### SendPulse

Can be useful for permission-based newsletter/contact-list management, but it should only be used after contacts are permission-based or clearly compliant.

Do not use for raw public outreach first.

## Daily sending rule

Target:

```text
8 lists × 30 contacts = 240/day
```

Delivery path:

- Public contact forms where available.
- One-to-one Gmail/manual email for public organization contacts.
- Email provider only after verified contacts and opt-out tracking are ready.

## Compliance lock

Every direct email needs:

- truthful subject line
- clear sender identity
- complete website links
- 100% free statement
- opt-out/remove line
- no attachments unless requested
- no misleading claims

## Future setup order

1. Finish source map.
2. Build daily tracker.
3. Prepare first 240 rows.
4. Send manually through public contact forms or one-to-one Gmail.
5. Track bounces, removes, replies, and not-fit responses.
6. Only then evaluate Mailjet for scale.
