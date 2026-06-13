---
name: marketing-system
description: >-
  Anna Hellmuth marketing design system (annahellmuth.com). Use when editing
  brand/, styleguide/, website/, or projects/ in MarketingSystem; creating
  social graphics, HTML templates, or static marketing pages; or when the user
  mentions burgundy/cream brand, or Source Serif 4.
---

# Marketing system — Anna Hellmuth

## First step

Read **[brand/DESIGN.md](brand/DESIGN.md)** — compact styling reference. Do not re-scrape or re-audit the live site unless the user requests a sync.

## Non-negotiables

- **Tokens:** `brand/tokens.css` only — no duplicate hex in sub-projects
- **Imports:** `tokens.css` + `typography.css` + `components.css`; add `website/css/site.css` for site chrome
- **Fonts:** Source Serif 4 (Google Fonts via `brand/typography.css`)
- **Legacy:** `projects/table/` orange palette is **not** the website brand

## Brand at a glance

| Item | Value |
|------|--------|
| Accent | `#64010d` (burgundy) |
| Text | `#5c020c` |
| Cream surface | `#f7eae3` |
| Heading font | Source Serif 4 600 |
| Body font | Source Serif 4 |
| Primary CTA | Schedule your discovery call |
| Service CTAs | Discover Counseling Services / Explore Coaching Details |

## Key components

- `.btn-primary` — burgundy pill
- `.services-card` + `.services-button` — white cards, full-width CTA
- `.testimonial-card` on `.section--burgundy` — white quote cards, grid layout
- `.section--cream` | `--white` | `--burgundy` — section backgrounds

## Repo

- `index.html` — **marketing center** (root hub — start here)
- `brand/index.html` — brand & marketing guides (all-in-one)
- `design-system/` — **component library** (all base UI components)
- `styleguide/` — visual brand preview + [marketing-guide.html](styleguide/marketing-guide.html)
- `website/` — static mirror; rebuild via `website/scripts/build-website.py`
- `brand/voice.md` — surface copy & CTAs
- `brand/marketing/` — positioning, audience, content, sales, messaging
- `brand/layouts.md` — 1080×1080, A4, etc.

## Marketing vs visual brand

| Need | Read |
|------|------|
| Colors, type, components | `brand/DESIGN.md` |
| CTAs, taglines, surface copy | `brand/voice.md` |
| Content posts, captions | `brand/marketing/content.md` + skill `content-writing` |
| Positioning, audience, sales | `brand/marketing/` + skill `marketing-strategy` |
| Social HTML templates | `projects/social/templates/` |

## When unsure

Open `styleguide/index.html` in browser or grep `brand/tokens.css` — do not invent new colors.
