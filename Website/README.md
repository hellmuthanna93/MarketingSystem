# Website — static mirror of annahellmuth.com

A static HTML copy of [annahellmuth.com](https://annahellmuth.com/) using the shared brand layer in [`../brand/`](../brand/).

## Pages

| Path | Live URL |
|------|----------|
| `index.html` | `/` |
| `counseling/` | `/counseling` |
| `lifecoaching/` | `/lifecoaching` |
| `about/` | `/about` |
| `contact/` | `/contact` |
| `blog/` | `/blog` |
| `blog/*/index.html` | Blog posts (4) |
| `impressum/` | `/impressum` |
| `privacy-policy/` | `/privacy-policy` |

## Preview locally

```bash
cd /Users/annahellmuth/Downloads/MarketingSystem
python3 -m http.server 8080
```

Open `http://localhost:8080/Website/`

## Rebuild from live site

When the Squarespace site changes, re-scrape and regenerate:

```bash
python3 Website/scripts/build-website.py
```

This fetches all sitemap pages, downloads images to `Website/assets/images/`, and writes HTML. Scraped structure is cached in `Website/data/pages.json`.

## Design system

- Layout & site chrome: [`css/site.css`](css/site.css) (imports `../../brand/*.css`)
- Tokens, typography, components: edit only in [`../brand/`](../brand/)
- Fonts: Google Fonts (Libre Baskerville) + Adobe Typekit (freight-text-pro) — see [`../brand/assets/fonts/README.md`](../brand/assets/fonts/README.md)

## Notes

- Contact/scheduling embeds from Squarespace are not mirrored; use mailto or link to the live booking flow on annahellmuth.com.
- Instagram feed blocks are omitted; social links point to your profiles.
- This is a static snapshot for marketing/offline use, not a replacement for Squarespace hosting.
