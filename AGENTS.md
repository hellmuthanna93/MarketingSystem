# AGENTS.md — MarketingSystem

Anna Hellmuth marketing design system (static HTML/CSS, no build step).

## Start here (token-efficient)

Read **[brand/DESIGN.md](brand/DESIGN.md)** for colors, type, components, and repo rules. Do not re-audit annahellmuth.com unless the user asks to sync from live.

| Need | File |
|------|------|
| **Marketing center (start here)** | [index.html](index.html) |
| **Business suite (internal operating manual)** | [business-site/index.html](business-site/index.html) · read [business-site/site/](business-site/site/) · source in [business-site/docs/](business-site/docs/) |
| Styling cheat sheet | [brand/DESIGN.md](brand/DESIGN.md) |
| Change tokens | [brand/tokens.css](brand/tokens.css) |
| Copy / CTAs | [brand/voice.md](brand/voice.md) |
| Marketing & content strategy | [brand/marketing/](brand/marketing/) |
| Social / print sizes | [brand/layouts.md](brand/layouts.md) |
| Visual preview | [styleguide/index.html](styleguide/index.html) |
| Component library | [design-system/index.html](design-system/index.html) |
| Brand & marketing hub (HTML) | [brand/index.html](brand/index.html) |
| Marketing guide (HTML) | [styleguide/marketing-guide.html](styleguide/marketing-guide.html) |
| Static website | [website/anna-hellmuth/](Website/anna-hellmuth/) — build: `python3 Website/anna-hellmuth/build-website.py` |
| Re-scrape live site | `python3 website/scripts/build-website.py` (legacy scraper; site is now src-driven) |

## Hard rules

1. **Never** hardcode brand hex in `projects/` or `website/` — use `brand/*.css` variables/classes.
2. **Only** edit palette in `brand/tokens.css`.
3. `projects/table/` uses a **legacy** orange palette; not the website brand until Phase 2.

## Cursor skills

| Skill | Use when |
|-------|----------|
| `.cursor/skills/marketing-system/` | Visual brand, HTML templates, tokens |
| `.cursor/skills/content-writing/` | Social posts, captions, blog drafts |
| `.cursor/skills/marketing-strategy/` | Positioning, audience, campaigns |
| `.cursor/skills/practice-profile/` | Canonical facts (pricing, services, credentials) — never invent |
| `.cursor/skills/practice-voice/` | Voice + humanizer pass for any client-facing copy |
| `.cursor/skills/discovery-calls/` · `wedge-clarity-session/` · `client-emails/` · `dach-mental-health-compliance/` · `case-studies-anonymized/` | Business-suite delivery & compliance |
