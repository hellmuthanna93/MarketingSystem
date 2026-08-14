---
name: Anna Hellmuth
description: Online psychological counseling and life coaching — burgundy/cream editorial practice brand
colors:
  accent: "#64010d"
  accent-hover: "#4a0202"
  burgundy: "#64010d"
  burgundy-hover: "#4a0202"
  gold: "#7d5e1f"
  gold-on-dark: "#d4a84a"
  text: "#5c020c"
  text-on-dark: "#ffffff"
  surface: "#f7eae3"
  surface-light: "#fefbf6"
  surface-card: "#ffffff"
  border-card: "rgba(100, 1, 13, 0.14)"
typography:
  display:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "clamp(2rem, 5vw, 3.5rem)"
    fontWeight: 600
    lineHeight: 1.35
  display-sm:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "clamp(1.8rem, 4.5vw, 3rem)"
    fontWeight: 600
    lineHeight: 1.35
  headline:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "clamp(1.6rem, 4vw, 2.5rem)"
    fontWeight: 600
    lineHeight: 1.3
  headline-lg:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "clamp(2.2rem, 4vw, 3.6rem)"
    fontWeight: 600
    lineHeight: 1.3
  title:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "clamp(1.25rem, 3vw, 1.75rem)"
    fontWeight: 600
    lineHeight: 1.35
  title-md:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "1.5rem"
    fontWeight: 600
    lineHeight: 1.35
  body:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "1.05rem"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "0.01em"
  body-lg:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "1.2rem"
    fontWeight: 400
    lineHeight: 1.8
  body-md:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "1.1rem"
    fontWeight: 400
    lineHeight: 1.7
  body-sm:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "1.15rem"
    fontWeight: 400
    lineHeight: 1.7
  label:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "0.9rem"
    fontWeight: 400
    letterSpacing: "0.05em"
  label-md:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "0.95rem"
    fontWeight: 400
  lead:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "clamp(1.15rem, 2vw, 1.35rem)"
    fontWeight: 400
    lineHeight: 1.7
  pullquote:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "clamp(1.4rem, 3vw, 1.9rem)"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  sm: "3px"
  md: "8px"
  card: "12px"
  panel: "16px"
  shell: "18px"
  option: "12px"
  pill: "300px"
  full: "50%"
spacing:
  2xs: "0.25rem"
  xs: "0.5rem"
  sm: "0.75rem"
  md: "1rem"
  lg: "1.5rem"
  xl: "2rem"
  2xl: "3rem"
  3xl: "4rem"
  section-y: "clamp(3rem, 8vw, 6rem)"
  section-x: "clamp(1rem, 4vw, 2.5rem)"
components:
  button-primary:
    backgroundColor: "{colors.burgundy}"
    textColor: "{colors.text-on-dark}"
    rounded: "{rounded.pill}"
    padding: "1.1rem 2rem"
    typography: "{typography.body}"
  button-primary-hover:
    backgroundColor: "{colors.burgundy-hover}"
    textColor: "{colors.text-on-dark}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.accent}"
    rounded: "{rounded.pill}"
    padding: "1.1rem 2rem"
  card-surface:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.text}"
    rounded: "{rounded.card}"
---

# Anna Hellmuth design system

<!-- impeccable:design-system-doc -->

## Overview

Warm editorial practice brand for annahellmuth.com: deep burgundy ink on cream paper, Source Serif 4 throughout, soft discovery-call CTAs. Visual authority lives in `brand/tokens.css` (palette only there). Public site CSS aliases tokens in `website/anna-hellmuth/assets/css/index.css`. Companion quick reference: `brand/DESIGN.md`.

## Colors

- **Accent / burgundy** `#64010d` — headings, links, solid fills for buttons and dark sections. Fills stay dark in both themes; accent ink lightens to rose in dark mode.
- **Text** `#5c020c` on cream; white on burgundy fills.
- **Surfaces** — light cream `#fefbf6` (primary), deeper cream `#f7eae3` (secondary), white cards.
- **Gold** `#7d5e1f` for marks and citations on cream (≥4.5:1); **gold-on-dark** `#d4a84a` for gold on burgundy fills.
- Never hardcode hex in `website/` or `projects/` — use CSS variables.

## Typography

Source Serif 4 for all roles (headings 600, body/UI/buttons 400). Fluid clamps for H1–H3. Prose measure ~42rem. Uppercase small nav labels with modest tracking.

## Layout

Max width `75rem`. Section vertical padding `clamp(3rem, 8vw, 6rem)`. Homepage heroes often center intro copy then split portrait + pull quote. Mobile collapses multi-column grids to single column under ~900px. Safe-area insets respected on body.

## Elevation & Depth

Soft ink-tinted shadows (`--shadow-soft`, `--shadow-card`). Frosted scrolled header uses light blur. Prefer tonal cream/burgundy layering over heavy chrome.

## Shapes

Pills for primary CTAs (`300px`). Cards ~12px; panels ~16px. Pull quotes use a **1px** accent border-inline-start (not thick side-tabs).

## Components

- **Primary button** — burgundy pill, white text, soft CTA label “Schedule your discovery call”.
- **Header** — tall absolute header that compresses when scrolled; mobile dialog with focus trap.
- **Service / testimonial cards** — cream/white surfaces, subtle burgundy borders.
- **Theme toggle** — fixed 44×44 control; dark theme tokens in `brand/tokens.css`.
- **Quiz** — progressbar with live status; options as large touch targets.

## Do's and Don'ts

**Do**
- Sell movement, not method; keep soft CTAs.
- Use practice-profile facts only; mark unknowns TBD.
- Prefer tokens and shared classes over inline styles.
- Respect `prefers-reduced-motion` for autoplay and reveals.

**Don't**
- Invent prices, credentials, testimonials, or outcome guarantees.
- Duplicate brand hex outside `brand/tokens.css`.
- Use thick (>1px) colored side borders as decoration.
- Shrink interactive targets below 44×44px on touch UIs.
