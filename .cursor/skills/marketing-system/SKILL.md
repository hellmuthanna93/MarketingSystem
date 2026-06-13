---
name: marketing-system
description: >-
  Anna Hellmuth marketing design system (annahellmuth.com). Use when editing
  brand/, styleguide/, website/, or projects/ in MarketingSystem; creating
  social graphics, HTML templates, or static marketing pages; or when the user
  mentions burgundy/cream brand, Libre Baskerville, or freight-text-pro.
---

# Marketing system — Anna Hellmuth

## First step

Read **[brand/DESIGN.md](brand/DESIGN.md)** — compact styling reference. Do not re-scrape or re-audit the live site unless the user requests a sync.

## Non-negotiables

- **Tokens:** `brand/tokens.css` only — no duplicate hex in sub-projects
- **Imports:** `tokens.css` + `typography.css` + `components.css`; add `website/css/site.css` for site chrome
- **Fonts:** Libre Baskerville (Google) + freight-text-pro (Typekit — see `brand/assets/fonts/README.md`)
- **Legacy:** `projects/table/` orange palette is **not** the website brand

## Brand at a glance

| Item | Value |
|------|--------|
| Accent | `#64010d` (burgundy) |
| Text | `#5c020c` |
| Cream surface | `#f7eae3` |
| Heading font | Libre Baskerville 700 |
| Body font | freight-text-pro |
| Primary CTA | Schedule your discovery call |
| Service CTAs | Discover Counseling Services / Explore Coaching Details |

## Key components

- `.btn-primary` — burgundy pill
- `.services-card` + `.services-button` — white cards, full-width CTA
- `.testimonial-card` on `.section--burgundy` — white quote cards, grid layout
- `.section--cream` | `--white` | `--burgundy` — section backgrounds

## Repo

- `styleguide/` — component preview
- `website/` — static mirror; rebuild via `website/scripts/build-website.py`
- `brand/voice.md` — copy
- `brand/layouts.md` — 1080×1080, A4, etc.

## When unsure

Open `styleguide/index.html` in browser or grep `brand/tokens.css` — do not invent new colors.
