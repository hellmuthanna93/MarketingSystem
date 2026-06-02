# Layout specs — marketing formats

Use brand tokens from `tokens.css` for all dimensions below. Safe zones assume text and logos stay **inset 48px** from edges unless noted.

## Social media

| Format | Size (px) | Notes |
|--------|-------------|--------|
| Instagram square | 1080 × 1080 | Feed post; keep CTA and logo in center 900×900 |
| Instagram portrait | 1080 × 1350 | Feed 4:5 |
| Instagram story / reel cover | 1080 × 1920 | Top/bottom 250px may be covered by UI |
| LinkedIn post | 1200 × 627 | Landscape; logo top-left |
| Facebook post | 1200 × 630 | Similar to LinkedIn |

**Backgrounds:** Prefer `--color-surface` or `--color-accent` with `--color-text` or `--color-text-on-dark` for contrast.

## Print & PDF

| Format | Size | Notes |
|--------|------|--------|
| A4 portrait | 210 × 297 mm | Handouts; 20mm margins |
| US Letter | 8.5 × 11 in | 0.75in margins |
| Business card | 85 × 55 mm | Logo + contact only |

Export HTML templates via browser **Print → Save as PDF** at 100% scale.

## Video (storyboards)

| Format | Size (px) | Notes |
|--------|-------------|--------|
| 16:9 | 1920 × 1080 | YouTube, webinars |
| 9:16 | 1080 × 1920 | Stories, TikTok, Reels |
| 1:1 | 1080 × 1080 | Square video |

Use burgundy (`--color-accent`) for lower-thirds and cream (`--color-surface`) for title cards. Body font: freight-text-pro; titles: Libre Baskerville.

## Tables & educational grids

- Max content width: `--layout-max-width`
- Minimum column width for dense grids: 150px (scroll horizontally on small screens)
- Phase 2: realign `projects/table/` to brand tokens (see root README)
