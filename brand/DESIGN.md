# Anna Hellmuth - Marketing design system (quick reference)

**Canonical source:** [annahellmuth.com](https://annahellmuth.com/) · **CSS source of truth:** `brand/tokens.css` (never duplicate hex in projects)

## Repo map

| Path | Role |
|------|------|
| `brand/` | Tokens, typography, components, voice, marketing, assets |
| `brand/index.html` | **HTML hub** - all brand & marketing guides in one page |
| `styleguide/` | Visual spec (`index.html`) |
| `design-system/` | Full component library (`index.html`, `css/`, `js/`) |
| `website/` | Static site mirror; uses `website/css/site.css` → imports brand |
| `projects/*` | Sub-projects; link `../../brand/*.css` by depth |

**Rule:** Change colors only in `brand/tokens.css`. Sub-projects import brand CSS; no inline palette.

---

## Colors

| Token | Hex | Use |
|-------|-----|-----|
| `--color-accent` | `#64010d` | Header, burgundy sections, primary buttons |
| `--color-accent-hover` | `#4a0202` | Button hover |
| `--color-text` | `#5c020c` | Headings & body on light backgrounds |
| `--color-text-on-dark` | `#ffffff` | Nav, text on burgundy |
| `--color-surface` | `#f7eae3` | Darker cream - testimonials, opportunity (`--color-bg-secondary`) |
| `--color-surface-light` | `#fefbf6` | Light cream - hero, services, steps, intake (`--color-bg-primary`) |
| `--color-border-card` | `rgba(100, 1, 13, 0.14)` | Service + testimonial cards |

**Squarespace HSL (for `hsla(var(--accent-hsl), …)`):** accent `352.73, 98.02%, 19.8%` · text `353.33, 95.74%, 18.43%`

---

## Typography

**Source Serif 4** ([Google Fonts](https://fonts.google.com/specimen/Source+Serif+4)) is used for all text - headings and body (`--font-heading` and `--font-body` both resolve to `--font-family`).

| Role | Weight | Token |
|------|--------|-------|
| Headings | 600 | `--font-weight-heading` |
| Body prose | 400 | `--font-weight-body` |
| Nav links | 400 | `--font-weight-ui` |
| Buttons | 400 | `--font-weight-button` |
| Labels, kickers, emphasis | 600 | `--font-weight-semibold` |
| Pricing, quote attribution | 500 | `--font-weight-medium` |

Source Serif 4 is a **variable font** (200-900) loaded from Google Fonts.

**Use CSS variables** from `brand/tokens.css` - never hardcode weights in `projects/`, `website/`, or `design-system/`.

**Load in HTML:** `tokens.css` + `typography.css` (Google Fonts `@import`). Optional preconnect - see `brand/assets/fonts/README.md`. Fallback: Georgia.

**Scale (desktop):** H2 ~2.8rem · H3 ~2rem · body 1rem · large body / `.sqsrte-large` ~1.2rem · service card body ~1.25rem

---

## Layout

- Max width: `75rem` (`--layout-max-width`)
- Prose column: `42rem` (`--layout-content-width`)
- Section padding: `clamp(3rem, 6vw, 5rem)` vertical · `clamp(1rem, 4vw, 2.5rem)` horizontal
- Homepage: centered headings; body often centered in intro blocks

**Section backgrounds (match Squarespace `data-section-theme`):**

| Class | BG | When |
|-------|-----|------|
| `.section--cream` | `#f7eae3` | `light` |
| `.section--white` | `#fff` | `white` |
| `.section--light` | `#fdf9f4` | alt light |
| `.section--burgundy` | `#64010d` | `dark` |

---

## Components

### Header
- Sticky burgundy bar; logo left; nav: Psychological counseling · Life coaching · About · Contact
- CTA in nav: **Schedule your discovery call** - compact `.nav-cta .btn-primary` (0.9rem, tight padding)
- No Blog link in header (blog at `/blog/`)

### Primary button `.btn-primary`
- Burgundy fill, white text, pill (`border-radius: 300px`), Source Serif 4 400, ~1.2rem
- Default padding: `--button-padding-y` / `--button-padding-x` (section CTAs)
- Nav variant: `--text-button-size-nav` + `--button-padding-*-nav` via `.nav-cta .btn-primary`

### Service cards `.services-card` + `.services-button`
- 2-column grid, white card, 20px radius, subtle burgundy border
- H3 burgundy, centered; full-width burgundy pill CTA below copy
- CTAs: **Discover Counseling Services** · **Explore Coaching Details**

### Testimonials `.testimonial-card` (on burgundy section)
- White cards, 12px radius, border `rgba(100,1,13,0.14)`
- Grid: 2 cols (`.testimonials-grid--2`) or 4fr/8fr (`.testimonials-grid--2-4-8`)
- Quote text `#5a1c1c`; cite **- Former client*** with 40px round avatar

### FAQ `.faq-details`
- White/cream section; `<details>` with +/− on summary; Source Serif 4 questions

### Links `.brand-link`
- Burgundy on light; white on burgundy sections

---

## Voice (short)

- Warm, understanding, confidently change-oriented; felt inner strength and compassion; not separate from the struggle - lived experience from the inside out; specialist who names the client's experience precisely; reader feels safe to trust you and that you'll get there together; clients respected as grown-ups; audience: **sensitive, thoughtful souls**
- **No-goes:** motivational slogans, downplaying experiences, pitying / collapsing into helplessness with the client, making yourself small, parent-to-child voice, coldness or showing off, name-dropping to impress
- Languages: EN, DE, UK, RU
- Primary CTA: **Schedule your discovery call**
- Full copy table: `brand/voice.md`

---

## HTML boilerplate (new static page)

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="stylesheet" href="../../brand/tokens.css" />
<link rel="stylesheet" href="../../brand/typography.css" />
<link rel="stylesheet" href="../../brand/components.css" />
<!-- optional site chrome: -->
<link rel="stylesheet" href="../../website/css/site.css" />
```

Adjust `../` depth per folder. See `brand/assets/fonts/README.md`.

---

## Out of brand (do not merge)

- `projects/table/` - legacy orange `#ff7a21` / gray `#6d7478` palette; Phase 2 realign to burgundy/cream

---

## Rebuild / preview

```bash
python3 -m http.server 8080   # → http://localhost:8080/styleguide/ or /website/
python3 website/scripts/build-website.py   # refresh static mirror from live site
```

**More detail:** `brand/AUDIT.md` · `brand/layouts.md` · `brand/tokens.reference.json`
