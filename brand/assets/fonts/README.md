# Fonts

The marketing system uses **Source Serif 4** from [Google Fonts](https://fonts.google.com/specimen/Source+Serif+4) for all text - headings and body.

## Load in HTML

Link brand CSS (the font loads via `@import` in `typography.css`):

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="stylesheet" href="../brand/tokens.css" />
<link rel="stylesheet" href="../brand/typography.css" />
<link rel="stylesheet" href="../brand/components.css" />
```

Adjust `../` depth per folder. No Adobe Typekit or other font services are required.

## Weights

Source Serif 4 variable font (**200-900**); headings **600**, buttons **400**. Semantic tokens in `brand/tokens.css` (`--font-weight-body`, `--font-weight-button`, etc.) map to these and intermediate values where needed.

## Fallback

If Google Fonts is unavailable, stacks fall back to Georgia (`brand/tokens.css`).

To self-host licensed fonts later, add files here and update `--font-family` in `tokens.css`.
