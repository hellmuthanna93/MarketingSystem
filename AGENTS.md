# AGENTS.md - MarketingSystem

Anna Hellmuth marketing design system (static HTML/CSS, no build step).

## Start here (token-efficient)

Read **[brand/DESIGN.md](brand/DESIGN.md)** for colors, type, components, and repo rules. Do not re-audit annahellmuth.com unless the user asks to sync from live.

| Need | File |
|------|------|
| **Marketing center (start here)** | [index.html](index.html) |
| **Business suite (internal operating manual)** | [business-site/index.html](business-site/index.html) · read [business-site/site/](business-site/site/) · source in [business-site/docs/](business-site/docs/) |
| Styling cheat sheet | [brand/DESIGN.md](brand/DESIGN.md) |
| Change tokens | [brand/tokens.css](brand/tokens.css) |
| Copy / CTAs | [brand/voice.md](brand/voice.md) |
| Marketing & content strategy | [brand/marketing/](brand/marketing/) |
| Social / print sizes | [brand/layouts.md](brand/layouts.md) |
| Visual preview | [styleguide/index.html](styleguide/index.html) |
| Component library | [design-system/index.html](design-system/index.html) |
| Brand & marketing hub (HTML) | [brand/index.html](brand/index.html) |
| Marketing guide (HTML) | [styleguide/marketing-guide.html](styleguide/marketing-guide.html) |
| Static website | [Website/anna-hellmuth/](Website/anna-hellmuth/) - build: `python3 Website/anna-hellmuth/build-website.py` (copies current brand CSS into its deployable `brand/` directory) · preview: `python3 -m http.server 8080 --directory Website/anna-hellmuth` → `http://localhost:8080/en/index.html` |
| Re-scrape live site | `python3 website/scripts/build-website.py` (legacy scraper; site is now src-driven) |

## Hard rules

1. **Never** hardcode brand hex in `projects/` or `website/` - use `brand/*.css` variables/classes.
2. **Only** edit palette in `brand/tokens.css`.
3. `projects/table/` uses a **legacy** orange palette; not the website brand until Phase 2.
4. **Website preview & deployment:** run the website build before previewing or uploading. It copies the shared brand CSS into `Website/anna-hellmuth/brand/`, so the `Website/anna-hellmuth/` folder can be served or uploaded as a self-contained site; preview `/en/index.html` from that folder.
5. **Website CSS references:** every generated website page must load the deployable, relative files from `src/templates/partials/head.html`: `../brand/tokens.css`, `../brand/typography.css`, `../brand/components.css`, and `../assets/css/index.css` for a top-level locale page. Do not link pages to the repository-root `brand/` directory. Keep the `<head>` partial as the single source of truth, then rebuild the site.
6. **Local preview URL:** serve `Website/anna-hellmuth/` itself and open `http://localhost:8080/en/...`. Do not preview the site through a repository-root URL such as `/website/anna-hellmuth/...`; that duplicate path can make it unclear whether the generated CSS and assets are current.
7. **GitHub commits (automatic):** after each completed change, commit the files changed for that task with a clear commit message and push to `origin` on the current branch. Do not wait for the user to ask. Never include unrelated pre-existing worktree changes. See `.cursor/rules/auto-commit-github.mdc`.
8. **Project roadmap (automatic):** after each completed user chat/task in this project, add a short dated entry to `roadmap.md` describing what was done, decided, or checked. Keep entries factual and concise; do not record unrelated chats or sensitive details.

## Cursor skills

| Skill | Use when |
|-------|----------|
| `.cursor/skills/marketing-system/` | Visual brand, HTML templates, tokens |
| `.cursor/skills/content-writing/` | Social posts, captions, blog drafts |
| `.cursor/skills/marketing-strategy/` | Positioning, audience, campaigns |
| `.cursor/skills/practice-profile/` | Canonical facts (pricing, services, credentials) - never invent |
| `.cursor/skills/practice-voice/` | Voice + humanizer pass for any client-facing copy |
| `.cursor/skills/discovery-calls/` · `wedge-clarity-session/` · `client-emails/` · `dach-mental-health-compliance/` · `case-studies-anonymized/` | Business-suite delivery & compliance |
