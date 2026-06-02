# Marketing System — Anna Hellmuth

A static, portable brand foundation for marketing materials based on [annahellmuth.com](https://annahellmuth.com/).

## Quick start

1. Open the styleguide in a browser:
   - **File:** open [`styleguide/index.html`](styleguide/index.html) directly, or
   - **Local server:** `python3 -m http.server 8080` from this folder, then visit `http://localhost:8080/styleguide/`
2. Edit brand tokens only in [`brand/tokens.css`](brand/tokens.css) (and sync [`brand/tokens.reference.json`](brand/tokens.reference.json) if you use it).
3. New sub-projects: copy the CSS links from the styleguide `<head>` and use relative paths to `brand/`.

## Folder map

```
brand/           Source of truth — tokens, typography, components, voice, assets
styleguide/      Visual reference (HTML)
Website/         Static mirror of annahellmuth.com (see Website/README.md)
projects/
  table/         Emotion table (legacy palette — Phase 2 realign)
  social/        Future social templates
  graphics/      Future print/PDF HTML
  video/         Future storyboard notes
```

## Rules

- **Do not** duplicate hex colors in project HTML — link `brand/*.css`.
- **Do** read [`brand/voice.md`](brand/voice.md) for copy and CTAs.
- **Do** read [`brand/layouts.md`](brand/layouts.md) for social/print/video dimensions.
- Audit notes: [`brand/AUDIT.md`](brand/AUDIT.md)

## Add a sub-project

```html
<link rel="stylesheet" href="../../brand/tokens.css" />
<link rel="stylesheet" href="../../brand/typography.css" />
<link rel="stylesheet" href="../../brand/components.css" />
```

Include the Typekit script from [`brand/assets/fonts/README.md`](brand/assets/fonts/README.md) if you need freight-text-pro to match the live site.

## Phase 2

Realign [`projects/table/`](projects/table/) from its orange/gray prototype palette to the burgundy/cream website brand.
