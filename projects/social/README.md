# Social media templates

HTML templates at fixed sizes (1080×1080, etc.).

## Templates

| File | Size | Use |
|------|------|-----|
| [templates/post-counseling.html](templates/post-counseling.html) | 1080×1080 | Counseling post - cream background, X→Y→Z formula |
| [templates/post-coaching.html](templates/post-coaching.html) | 1080×1080 | Coaching post - burgundy background, X→Y→Z formula |
| [templates/post-quote.html](templates/post-quote.html) | 1080×1080 | Testimonial-style quote card |

**Before building or editing:**

1. Link styles from `../../brand/` (see root README).
2. Read [`brand/layouts.md`](../../brand/layouts.md) for dimensions and safe zones (48px inset).
3. Read [`brand/marketing/content.md`](../../brand/marketing/content.md) for the content checklist and post formula.
4. Use [`brand/voice.md`](../../brand/voice.md) for CTAs.

## Workflow

1. Duplicate a template or edit placeholder copy in place.
2. Open in browser at exact viewport (1080×1080).
3. Export via screenshot or browser capture at 1× scale.

**Preview:** `python3 -m http.server 8080` from repo root → `http://localhost:8080/projects/social/templates/post-counseling.html`
