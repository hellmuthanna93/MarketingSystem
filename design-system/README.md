# Design system - Anna Hellmuth

Static HTML/CSS/JS component library extracted from [annahellmuth.com](https://annahellmuth.com/) patterns.

## Preview

```bash
python3 -m http.server 8080
```

Open [http://localhost:8080/design-system/](http://localhost:8080/design-system/)

## Structure

```
design-system/
  index.html           Component gallery & documentation
  css/
    foundation.css     Reset, a11y, layout, showcase chrome
    components.css     All UI components (website-aligned)
  js/
    design-system.js   Header, mobile nav, sliders
```

## CSS imports (new pages)

```html
<link rel="stylesheet" href="../brand/tokens.css" />
<link rel="stylesheet" href="../brand/typography.css" />
<link rel="stylesheet" href="../brand/components.css" />
<link rel="stylesheet" href="../design-system/css/foundation.css" />
<link rel="stylesheet" href="../design-system/css/components.css" />
```

Source Serif 4 loads via `brand/typography.css` (Google Fonts). See [brand/assets/fonts/README.md](../brand/assets/fonts/README.md).

## Component index

| Category | Classes |
|----------|---------|
| **Typography** | `.text-display`, `.text-h2`, `.text-body`, `.text-small`, `.text-on-dark` |
| **Buttons** | `.btn-primary`, `.btn-secondary`, `.btn-light`, `.btn-ghost`, `--sm` size |
| **Links** | `.brand-link`, `.btn-ghost`, nav underline links |
| **Forms** | `.form-field`, `.form-label`, `.form-input`, `.form-textarea`, `.form-select`, `.form-check` |
| **Badges** | `.badge`, `.pricing-badge` |
| **Alerts** | `.alert`, `.alert--info`, `.alert--success` |
| **Layout** | `.container`, `.section`, `.section--cream/burgundy/light`, `.bg-dark` |
| **Hero** | `.hero`, `.hero-grid`, `.hero-subtitle`, `.hero-image-wrapper` |
| **Cards** | `.service-card`, `.about-card`, `.pricing-card`, `.contact-prompt` |
| **Testimonials** | `.testimonial-card`, `.quote-testimonial`, `[data-slider]` |
| **Steps** | `.step-circle`, `.steps-grid`, `.step-card`, `.steps-list` |
| **FAQ** | `.accordion-list`, `.accordion-item` (`<details>`) |
| **Lists** | `.checklist`, `.opportunity-list`, `.pricing-features` |
| **Quote** | `.quote-banner` |
| **Navigation** | `.site-header`, `.nav-links`, `.nav-toggle`, `.mobile-menu` |
| **Footer** | `.site-footer`, `.footer-grid`, `.social-icon` |
| **Utilities** | `.breadcrumb`, `.divider`, `.sr-only`, `.skip-link` |

## Rules

- Edit colors only in `brand/tokens.css`
- Class names match the website mirror where possible - drop-in compatible
- All interactive patterns use native HTML first (`<details>`, `aria-*`, keyboard support)

## Related

- [brand/DESIGN.md](../brand/DESIGN.md) - token cheat sheet
- [styleguide/index.html](../styleguide/index.html) - compact visual reference
- [brand/index.html](../brand/index.html) - marketing & brand hub
