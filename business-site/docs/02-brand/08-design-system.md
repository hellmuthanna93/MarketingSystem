# Design System

> **Pointer doc.** The component library is [design-system/index.html](../../../design-system/index.html); the styling cheat sheet is [brand/DESIGN.md](../../../brand/DESIGN.md); components live in [brand/components.css](../../../brand/components.css). Do not duplicate styles — link the brand CSS.

## What exists

| Asset | Location |
|-------|----------|
| Full component library (HTML) | [design-system/index.html](../../../design-system/index.html) |
| Visual styleguide | [styleguide/index.html](../../../styleguide/index.html) |
| Tokens (colors, spacing, type, radius, shadow) | [brand/tokens.css](../../../brand/tokens.css) |
| Typography (Source Serif 4 via Google Fonts) | [brand/typography.css](../../../brand/typography.css) |
| Components (buttons, cards, sections, nav, etc.) | [brand/components.css](../../../brand/components.css) |

## Key components (for any studio-owned surface)

- `.btn-primary` — burgundy pill, white text, Source Serif 4 400
- `.btn-light` — outline variant for dark backgrounds
- `.services-card` + `.services-button` — white cards with full-width CTA
- `.testimonial-card` on `.section--burgundy` — white quote cards
- `.section--cream` / `--white` / `--light` / `--burgundy` — section backgrounds
- `.faq-details` — `<details>` accordion
- `.brand-link` — context-aware link color

## HTML boilerplate for a new suite page

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="stylesheet" href="../../brand/tokens.css" />
<link rel="stylesheet" href="../../brand/typography.css" />
<link rel="stylesheet" href="../../brand/components.css" />
```

Adjust `../` depth per folder. The suite's render pages (`business-site/render/`) use this pattern with two-level depth (`../../brand/...`).

## Rules

- Edit palette only in `brand/tokens.css`
- Never hardcode hex in suite/render/projects HTML
- Reuse existing components before inventing new ones

## So what

The suite reuses the existing, mature design system rather than building a parallel one. Any HTML in this suite (dashboard, render pages) inherits the burgundy/cream, Source Serif 4 brand automatically. Detail: [brand/DESIGN.md](../../../brand/DESIGN.md).
