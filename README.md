# Marketing System — Anna Hellmuth

A static, portable brand foundation for marketing materials based on [annahellmuth.com](https://annahellmuth.com/).

## Quick start

1. Open the **Marketing Center** in a browser:
   - **Hub:** [`index.html`](index.html) — links to everything
   - **Business suite:** [`business-site/index.html`](business-site/index.html) — internal operating manual (strategy → toolkit), source in [`business-site/docs/`](business-site/docs/)
   - **Brand hub:** [`brand/index.html`](brand/index.html) — all guides in one page
   - **Styleguide:** [`styleguide/index.html`](styleguide/index.html)
   - **Design system:** [`design-system/index.html`](design-system/index.html) — full component library
   - **Local server:** `python3 -m http.server 8080` from this folder, then visit `http://localhost:8080/`
2. Edit brand tokens only in [`brand/tokens.css`](brand/tokens.css) (and sync [`brand/tokens.reference.json`](brand/tokens.reference.json) if you use it).
3. New sub-projects: copy the CSS links from the styleguide `<head>` and use relative paths to `brand/`.

## Folder map

```
brand/           Source of truth — tokens, typography, components, voice, marketing, assets
  marketing/     Positioning, audience, content guidelines, sales, messaging
styleguide/      Visual + marketing reference (HTML)
design-system/   Full component library (HTML/CSS/JS)
website/         Static site — see website/README.md (`anna-hellmuth/`)
projects/
  table/         Emotion table (legacy palette — Phase 2 realign)
  social/        Future social templates
  graphics/      Future print/PDF HTML
  video/         Future storyboard notes
```

## Rules

- **Do not** duplicate hex colors in project HTML — link `brand/*.css`.
- **Agents:** start with [`brand/DESIGN.md`](brand/DESIGN.md) or [`AGENTS.md`](AGENTS.md) (styling cheat sheet — saves re-auditing the live site).
- **Do** read [`brand/voice.md`](brand/voice.md) for copy and CTAs.
- **Do** read [`brand/marketing/`](brand/marketing/) for positioning, content strategy, and audience.
- **Do** read [`brand/layouts.md`](brand/layouts.md) for social/print/video dimensions.
- Audit notes: [`brand/AUDIT.md`](brand/AUDIT.md)

## Add a sub-project

```html
<link rel="stylesheet" href="../../brand/tokens.css" />
<link rel="stylesheet" href="../../brand/typography.css" />
<link rel="stylesheet" href="../../brand/components.css" />
```

Source Serif 4 loads via `brand/typography.css` (Google Fonts). See [`brand/assets/fonts/README.md`](brand/assets/fonts/README.md).

## Phase 2

Realign [`projects/table/`](projects/table/) from its orange/gray prototype palette to the burgundy/cream website brand.
