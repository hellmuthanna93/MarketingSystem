# Tools & Stack

A lean online stack. Every tool that touches client data must be GDPR-safe with a DPA/AVV in place (see [../04-marketing/06-outreach-compliance-germany.md](../04-marketing/06-outreach-compliance-germany.md)). Tools below reflect current/known usage and sensible defaults; confirm and fill TBDs.

## Current / known

| Function | Tool | Notes |
|----------|------|-------|
| Discovery booking | Google Calendar appointments | calendar.app.google/ueKb9RbyxWyC6zfK8 |
| Website | annahellmuth.com (Squarespace) + static mirror in repo | Brand CSS in `brand/` |
| Email | contact@annahellmuth.com | Logistics + client comms |
| Social | Instagram, LinkedIn, TikTok, Facebook | See [../04-marketing/03-channels.md](../04-marketing/03-channels.md) |
| Directory | Location Independent Therapists | Passive inbound |

## Recommended stack (confirm / TBD)

| Function | Option | DPA needed? |
|----------|--------|-------------|
| Video sessions | Zoom (EU data option) or equivalent | Yes |
| Payments | Stripe / Wise / SEPA | Yes |
| Booking + payment for wedge/packages | Calendar tool with payment, or Stripe link | Yes |
| Session notes | Encrypted/EU-hosted notes (TBD) | Yes — health data |
| Newsletter | Double-opt-in provider (e.g. EU-based) | Yes |
| Intake forms | GDPR-safe form tool | Yes — health data |
| Async video (summaries, welcome) | Loom or similar | Yes if client data |
| Content scheduling | Buffer/Later or native | No client data |

## Selection principles

- **GDPR first** — prefer EU-hosted or DPA-covered providers; client/health data is special category.
- **Simple over sprawling** — fewer tools, less admin, more free time.
- **Reliability** — sessions and payments must just work.
- **Brand consistency** — client-facing surfaces use `brand/*.css`.

## Data hygiene

- Keep client data only in DPA-covered tools.
- Minimize what's collected; retain per the privacy policy.
- Never paste identifiable client material into non-covered tools (incl. AI tools).

## So what

A small, GDPR-safe stack runs the whole practice: book → pay → meet → note → follow up. The action item is confirming each tool has a DPA and an EU-data option. Tracked in [../08-roadmap/04-task-backlog.md](../08-roadmap/04-task-backlog.md). Workflow that uses it: [02-delivery-workflow.md](02-delivery-workflow.md).
