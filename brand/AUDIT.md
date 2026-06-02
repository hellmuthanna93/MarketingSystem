# Brand audit — annahellmuth.com

**Source:** [annahellmuth.com](https://annahellmuth.com/) (Squarespace, Fluid Engine)  
**Audited:** 2026-06-02 (computed styles + Squarespace theme variables)

## Colors

| Token (semantic) | Hex | HSL (Squarespace) | Usage on site |
|------------------|-----|-------------------|---------------|
| Accent / primary | `#64010d` | `352.73, 98.02%, 19.8%` | Hero background, primary buttons, header on dark sections |
| Text | `#5c020c` | `353.33, 95.74%, 18.43%` | Headings and body on cream sections |
| Text on dark | `#ffffff` | `0, 0%, 100%` | Navigation and buttons on burgundy |
| Surface (cream) | `#f7eae3` | `21, 55.56%, 92.94%` (darkAccent) | Main content section backgrounds |
| Surface light | `#fdf9f4` | `37.5, 80%, 98.04%` (lightAccent) | Lighter accent surfaces |

## Typography

| Role | Family | Weight | Size (desktop sample) |
|------|--------|--------|------------------------|
| Headings | Libre Baskerville (Google) | 700 | H2 ~45px / 58px line-height; H3 ~32px |
| Body & UI | freight-text-pro (Adobe Typekit) | 400 body, 600 nav/buttons | Body ~13–16px; buttons ~19px |

**Typekit kit:** Same script as live site (`use.typekit.net` — site owner kit). Fallbacks: Georgia, serif for headings; system sans if Typekit unavailable.

## Spacing & layout

- Content max width: ~1200px (marketing approximation; Squarespace fluid sections vary)
- Section padding: ~4vw horizontal on mobile, generous vertical rhythm between blocks
- Button padding: ~25px × ~38px; pill shape (`border-radius: 300px`)

## Components (live site)

- **Primary CTA:** Solid burgundy pill, white label, freight-text-pro semibold — “Schedule your discovery call”
- **Service cards:** H3 + short description, secondary CTAs (“Discover Counseling Services”)
- **Testimonials:** Long quotes, attribution “— Former client*”
- **FAQ:** Accordion with H3 questions
- **Steps:** Numbered journey (“Step 1… Step 2… Step 3…”)

## Voice (summary)

- Warm, professional, empowering; speaks to “creative & ambitious souls”
- Multilingual practice: English, German, Ukrainian, Russian
- Primary CTA: “Schedule your discovery call”

## Assets captured

- Logo: `brand/assets/logo/logo.png` (from Squarespace CDN)

## Not in brand tokens (legacy)

The `projects/table/` emotion table uses a separate orange/gray palette — **Phase 2** realign to this audit.
