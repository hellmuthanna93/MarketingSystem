# Anna Hellmuth — Business Suite

A complete **business operating system** for Anna Hellmuth's online psychological counseling and life coaching practice — strategy, brand, offerings, marketing, sales, operations, finance/legal, roadmap, and a copy-paste execution toolkit.

This is **not** the public website (that lives in [`../Website/anna-hellmuth/`](../Website/anna-hellmuth/)). This is the internal manual for running and growing the practice.

## How it works

- **`docs/` is the source of truth.** Markdown, edited by Anna or an agent. Organized into 9 numbered domains plus an overview.
- **`site/` is generated HTML** for easier reading and review. Run `python3 build-html.py` after editing markdown (requires `pip3 install -r requirements.txt`).
- **Card dashboard** at [`index.html`](index.html) links into the designed pages. **Sidebar reader** at [`site/index.html`](site/index.html) lists every doc with on-page navigation, table of contents, and theme toggle.
- **Skills enforce quality.** New agent skills in [`../.cursor/skills/`](../.cursor/skills/) (`practice-profile`, `practice-voice`, `discovery-calls`, `wedge-clarity-session`, `client-emails`, `dach-mental-health-compliance`, `case-studies-anonymized`) keep facts and voice consistent. The rule `../.cursor/rules/voice-mandatory.mdc` makes agents read them before writing copy.

## Start here

| Need | File |
|------|------|
| Card dashboard | [index.html](index.html) |
| Designed doc reader (all pages) | [site/index.html](site/index.html) |
| The thesis | [site/00-overview.html](site/00-overview.html) |
| Who we serve & why we're credible | [site/01-strategy/](site/01-strategy/) |
| What we sell (incl. the Clarity Session wedge) | [site/03-offerings/](site/03-offerings/) |
| How we get clients | [site/04-marketing/](site/04-marketing/) |
| Ready-to-use posts, scripts, templates | [site/09-toolkit/](site/09-toolkit/) |
| What to do next | [site/08-roadmap/01-90-day-launch.html](site/08-roadmap/01-90-day-launch.html) |

## Preview locally

From the repo root:

```bash
pip3 install -r business-site/requirements.txt
python3 business-site/build-html.py
python3 -m http.server 4173
```

Open [http://localhost:4173/business-site/site/00-overview.html](http://localhost:4173/business-site/site/00-overview.html) or the [card dashboard](http://localhost:4173/business-site/index.html).

## Section map

| # | Domain | Contents |
|---|--------|----------|
| 00 | Overview | Thesis, north star, operating principles, section map |
| 01 | Strategy | Vision, positioning, ICP, market, SWOT, business model, pricing, business plan |
| 02 | Brand | Brand strategy, naming, visual identity, voice, messaging, logo, voice reference, design system (mostly pointers to `brand/`) |
| 03 | Offerings | Service catalog, **Clarity Session wedge**, packages, products, case-study strategy |
| 04 | Marketing | Strategy, content engine, channels, lead gen, website plan, compliance, outreach, funnel, international |
| 05 | Sales | Process, discovery-to-wedge, counseling agreement, onboarding |
| 06 | Operations | Tools, delivery workflow, SOPs, quality bar |
| 07 | Finance & Legal | DACH legal setup, finance model, runway, templates, projections |
| 08 | Roadmap | 90-day launch, transition, milestones/KPIs, master backlog |
| 09 | Toolkit | Discovery script, social posts, content calendar, emails, deliverable + agreement + invoice templates |

## Maintenance

1. Edit `docs/**/*.md` (with skills loaded).
2. Run `python3 business-site/build-html.py` to refresh `site/`.
3. Update `practice-profile` skill when pricing/offers/facts change.
4. Track execution in [docs/08-roadmap/04-task-backlog.md](docs/08-roadmap/04-task-backlog.md).
5. Extend the toolkit by adding numbered files in `docs/09-toolkit/`, then rebuild.

## Conventions

- Facts/prices come only from `practice-profile`. Unknowns are **TBD**.
- The **Clarity Session** wedge is **proposed/TBD** — not published until Anna confirms name, price, and promise.
- Legal/finance content is DACH-specific and **not legal advice**; confirm with a professional.
- No brand hex in HTML — link `../brand/tokens.css`, `typography.css`, `components.css`.
- Do not hand-edit `site/` — it is wiped and regenerated on each build.
