# Website — annahellmuth.com (static, multilingual)

Static site for [annahellmuth.com](https://annahellmuth.com/), built from `src/` into locale folders `en/`, `de/`, `uk/`, `ru/`.

## Build (required after editing content)

From `Website/anna-hellmuth/`:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python build-website.py
```

Single locale (faster iteration):

```bash
.venv/bin/python build-website.py --locale de
```

**Do not hand-edit** generated HTML in `en/`, `de/`, `uk/`, `ru/`, or root `index.html`. Edit source in `src/` and rebuild.

## Source layout

| Path | Purpose |
|------|---------|
| `src/templates/` | Jinja layout (header, footer, language switcher) |
| `src/locales/{en,de,uk,ru}/site.yaml` | Nav labels, CTAs, footer copy per locale |
| `src/locales/{locale}/bodies/*.html.j2` | Page main content (Jinja) |
| `src/pages-manifest.yaml` | Translation keys, slugs, titles |
| `src/shared/` | Contact URL, pricing (from practice-profile) |
| `assets/` | Images, CSS, JS (shared) |

## Preview

From the **repo root**:

```bash
python3 -m http.server 8080
```

Open [http://localhost:8080/Website/anna-hellmuth/en/](http://localhost:8080/Website/anna-hellmuth/en/)

Root `index.html` redirects to `/en/`.

## Locales

| Code | Language | Example URL |
|------|----------|-------------|
| `en` | English | `/en/counseling.html` |
| `de` | German | `/de/psychologische-beratung.html` |
| `uk` | Ukrainian | `/uk/psychologichne-konsultuvannya.html` |
| `ru` | Russian | `/ru/psihologicheskoe-konsultirovanie.html` |

Each page includes `hreflang` alternates and a header language switcher (EN · DE · UK · RU).

## Legacy URLs

When deploying, configure **301 redirects** from old flat paths (e.g. `/counseling.html` → `/en/counseling.html`). See [REDIRECTS.md](REDIRECTS.md).

## Styling

Pages import the shared brand system (`../../brand/` from locale pages). Site-specific CSS: `assets/css/index.css`. Edit colors only in `brand/tokens.css`.

## Localization workflow

1. Edit English bodies in `src/locales/en/bodies/`
2. Add/adapt strings in `src/generate_locale_bodies.py` or edit `de`/`uk`/`ru` bodies directly
3. Run `build-website.py`
4. Native-speaker review before publishing non-EN copy
