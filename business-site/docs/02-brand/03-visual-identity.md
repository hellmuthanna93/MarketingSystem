# Visual Identity Direction

> **Pointer doc.** The visual identity source of truth is [brand/DESIGN.md](../../../brand/DESIGN.md), with tokens in [brand/tokens.css](../../../brand/tokens.css). Do not duplicate hex values here or anywhere - link the brand CSS.

## At a glance

| Element | Value | Token |
|---------|-------|-------|
| Accent (burgundy) | `#64010d` | `--color-accent` |
| Accent hover | `#4a0202` | `--color-accent-hover` |
| Text | `#5c020c` | `--color-text` |
| Cream surface (darker) | `#f7eae3` | `--color-surface` |
| Cream surface (light) | `#fefbf6` | `--color-surface-light` |
| Text on dark | `#ffffff` | `--color-text-on-dark` |

## Typography

**Source Serif 4** for everything - headings and body (variable font, 200-900, via Google Fonts in [brand/typography.css](../../../brand/typography.css)).

- Headings: weight 600
- Body: 400
- Labels/kickers/emphasis: 600
- Pricing/quote attribution: 500
- Fallback: Georgia

## Layout principles

- Max width `75rem`; prose column `42rem`
- Section padding `clamp(3rem, 6vw, 5rem)` vertical
- Centered headings on homepage; flowing prose
- Section backgrounds: `.section--cream` / `--white` / `--light` / `--burgundy`

## Photography / illustration direction

- Calm, warm, human; natural light; uncluttered
- Feminine, grounded, premium - never stocky "happy business people" or clinical sterility
- Burgundy/cream palette harmony in any custom graphics
- The logo and existing site imagery set the reference

## Rule

Per `AGENTS.md`: never hardcode brand hex in sub-projects. Always link `../../brand/tokens.css`, `typography.css`, `components.css` (adjust depth). Edit palette **only** in `brand/tokens.css`.

## So what

The look is established and consistent: burgundy + cream, Source Serif 4, calm premium. Any new surface (wedge page, render pages, graphics) inherits it via the brand CSS. Full detail and HTML boilerplate: [brand/DESIGN.md](../../../brand/DESIGN.md).
