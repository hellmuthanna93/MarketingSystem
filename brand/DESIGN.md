# Anna Hellmuth — Marketing design system (quick reference)

**Canonical source:** [annahellmuth.com](https://annahellmuth.com/) · **CSS source of truth:** `brand/tokens.css` (never duplicate hex in projects)

## Repo map

| Path | Role |
|------|------|
| `brand/` | Tokens, typography, components, voice, assets |
| `styleguide/` | Visual spec (`index.html`) |
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
| `--color-surface` | `#f7eae3` | Cream sections (SQ `light` theme) |
| `--color-surface-light` | `#fdf9f4` | Lighter panels |
| White sections | `#ffffff` | Service cards area (SQ `white` theme) |
| Testimonial card text | `#5a1c1c` | On white cards |
| Card border | `rgba(100, 1, 13, 0.14)` | Services + testimonials |

**Squarespace HSL (for `hsla(var(--accent-hsl), …)`):** accent `352.73, 98.02%, 19.8%` · text `353.33, 95.74%, 18.43%`

---

## Typography

| Role | Font | Weight |
|------|------|--------|
| Headings | Libre Baskerville (Google) | 700 |
| Body, nav, buttons | freight-text-pro (Typekit) | 400 / 600 |

**Load in HTML:** Google Fonts link in `typography.css` + Typekit script from `brand/assets/fonts/README.md` (same kit as live site). Fallback: Georgia.

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
- CTA in nav: **Schedule your discovery call** (pill `.btn-primary`)
- No Blog link in header (blog at `/blog/`)

### Primary button `.btn-primary`
- Burgundy fill, white text, pill (`border-radius: 300px`), freight 600, ~1.2rem, generous padding

### Service cards `.services-card` + `.services-button`
- 2-column grid, white card, 20px radius, subtle burgundy border
- H3 burgundy, centered; full-width burgundy pill CTA below copy
- CTAs: **Discover Counseling Services** · **Explore Coaching Details**

### Testimonials `.testimonial-card` (on burgundy section)
- White cards, 12px radius, border `rgba(100,1,13,0.14)`
- Grid: 2 cols (`.testimonials-grid--2`) or 4fr/8fr (`.testimonials-grid--2-4-8`)
- Quote text `#5a1c1c`; cite **— Former client*** with 40px round avatar

### FAQ `.faq-details`
- White/cream section; `<details>` with +/− on summary; Libre Baskerville questions

### Links `.brand-link`
- Burgundy on light; white on burgundy sections

---

## Voice (short)

- Warm, professional, empowering; audience: **creative & ambitious souls**
- Languages: EN, DE, UK, RU
- Primary CTA: **Schedule your discovery call**
- Full copy table: `brand/voice.md`

---

## HTML boilerplate (new static page)

```html
<link rel="stylesheet" href="../../brand/tokens.css" />
<link rel="stylesheet" href="../../brand/typography.css" />
<link rel="stylesheet" href="../../brand/components.css" />
<!-- optional site chrome: -->
<link rel="stylesheet" href="../../website/css/site.css" />
```

Adjust `../` depth per folder. For freight-text-pro, add Typekit script (see `brand/assets/fonts/README.md`).

---

## Out of brand (do not merge)

- `projects/table/` — legacy orange `#ff7a21` / gray `#6d7478` palette; Phase 2 realign to burgundy/cream

---

## Rebuild / preview

```bash
python3 -m http.server 8080   # → http://localhost:8080/styleguide/ or /website/
python3 website/scripts/build-website.py   # refresh static mirror from live site
```

**More detail:** `brand/AUDIT.md` · `brand/layouts.md` · `brand/tokens.reference.json`
