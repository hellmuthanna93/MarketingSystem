# Business Suite Replication Plan & Full Inventory

> **Purpose:** Hand this document to an AI agent (or human team) building the same kind of extensive operating manual for **another solo or small professional services business**.  
> **Source reference:** Design Engineering Studio repo - `docs/` (source of truth) + `site/` (generated HTML view) + `agents/skills/` (portable agent instructions).  
> **Last inventoried:** June 2026

---

## 1. What you are replicating

This is not a marketing website. It is a **complete business operating system** for launching and running a premium solo consultancy:

| Layer | Role |
| --- | --- |
| **`docs/`** | Markdown source of truth - strategy, brand, sales, ops, finance, roadmap, and copy-paste toolkit |
| **`site/`** | Generated, styled HTML documentation site for reading, sharing, and printing |
| **`agents/skills/`** | Portable Agent Skills that enforce voice, facts, and channel-specific output quality |
| **`build.mjs`** | Static site generator: Markdown → themed HTML with sidebar nav, TOC, Mermaid, dark mode |
| **`.cursor/rules/`** | IDE rule that forces agents to read skills before writing any client-facing copy |

**Scale achieved (v1):**

- **64 Markdown documents** (~6,900 lines total)
- **65 HTML pages** (64 docs + dashboard)
- **9 numbered domains** + overview + toolkit
- **90+ ready-to-publish social posts** across LinkedIn and Instagram
- **11 agent skills** composable for proposals, outreach, audits, discovery calls, case studies
- **Breadth-first:** every business domain has an actionable starting doc; depth grows over time

**Design philosophy:**

1. **Markdown first** - agents and humans edit `.md`; HTML is disposable output.
2. **Numbered sections** - forces a logical build order (strategy before marketing before sales).
3. **Strategy + execution split** - sections 01-08 are thinking; section 09 is copy-paste assets.
4. **One thesis, many layers** - overview doc holds the mental model; everything else drills down.
5. **Operating principles as guardrails** - when in doubt, docs point back to principles in `00-overview`.
6. **Compound assets** - every engagement should produce a case study, template, or content piece.

---

## 2. Architecture (build this first)

### 2.1 Repository layout

```
project-root/
├── README.md                 # Dashboard intro (also rendered as site/index.html body)
├── package.json              # { "dependencies": { "marked": "^12" }, "scripts": { "build": "node build.mjs" } }
├── build.mjs                 # Static site generator (see §2.3)
├── assets/
│   └── styles.css            # Suite chrome (sidebar, prose, cards, TOC) - NOT regenerated
├── docs/                     # SOURCE OF TRUTH - agent edits here
│   ├── 00-overview.md
│   ├── 01-strategy/
│   ├── 02-brand/
│   ├── 03-offerings/
│   ├── 04-marketing/
│   ├── 05-sales/
│   ├── 06-operations/
│   ├── 07-finance-legal/
│   ├── 08-roadmap/
│   └── 09-toolkit/
├── site/                     # GENERATED - do not hand-edit; run npm run build
│   ├── index.html
│   ├── 00-overview.html
│   ├── 01-strategy/ … 09-toolkit/
│   └── assets/
│       ├── styles.css
│       └── design-system/    # tokens.css + motion.css copied at build
├── agents/skills/            # Portable skills (studio-profile, studio-voice, channel skills)
└── .cursor/rules/voice.mdc   # Mandatory skill workflow for copy generation
```

Optional but recommended alongside the suite:

- **`website/`** - public lead-gen site (separate from internal business suite)
- **`AGENT-PLAYBOOK.md`** - brainstorm of agent-driven tasks that extend the suite
- **`media/`** - images referenced from docs (logo concepts, etc.; copied to `site/media/` at build)

### 2.2 HTML site features (what `build.mjs` produces)

Each page includes:

- **Fixed sidebar** with 9 section groups + Start (Dashboard, Overview)
- **Brand block** (logo SVG + business name + subtitle)
- **Theme toggle** (light/dark, persisted in `localStorage`)
- **External link** to public website
- **Mobile menu** toggle
- **On-page TOC** (auto-generated from `##` and `###` headings when ≥3 exist)
- **Prose styling** for headings, lists, blockquotes, code, tables
- **Mermaid diagrams** rendered client-side (flowcharts in strategy, funnel, wedge offer)
- **Internal link rewriting** - `.md` → `.html` automatically
- **Dashboard cards** - README content + one card per section listing all pages

Tech stack: **zero framework**, one npm dependency (`marked`), Google Fonts (Inter + JetBrains Mono), Mermaid 11 from CDN.

### 2.3 Build script responsibilities

`build.mjs` must:

1. Delete and recreate `site/`
2. Copy `assets/styles.css` and design tokens from your public design system
3. Walk all `docs/**/*.md`, sort by section order then filename
4. Parse Markdown with GFM; special-case ` ```mermaid ` blocks
5. Inject heading `id` attributes for TOC anchors
6. Render shared sidebar with active page highlight
7. Write one HTML file per Markdown file (same path, `.html` extension)
8. Generate `index.html` from root `README.md` + section dashboard cards

Commands:

```bash
npm install
npm run build          # → site/
npm run serve          # build + python http.server on :4173
```

---

## 3. Complete document inventory

### Start (2 pages)

| File | Title | Purpose |
| --- | --- | --- |
| `README.md` → `index.html` | Dashboard | Repo intro, build instructions, section card grid |
| `00-overview.md` | Studio Overview | Thesis, north star, unfair advantages, operating principles, section map (Mermaid) |

### 01 · Strategy (8 pages)

| File | Title | Key contents |
| --- | --- | --- |
| `01-vision-mission-values.md` | Vision, Mission & Values | Long-term vision, mission statement, core values |
| `02-positioning-and-niche.md` | Positioning & Niche | Wedge definition, niche tiers (primary/secondary/tertiary), positioning axes, positioning test |
| `03-ideal-client-profile.md` | Ideal Client Profile | Segments, firmographics, psychographics, triggers, anti-ICP |
| `04-market-and-competitors.md` | Market & Competitor Analysis | DACH/EU context, day-rate landscape, buyer alternatives, direct competitors, market risks |
| `05-swot.md` | SWOT Analysis | Strengths/weaknesses/opportunities/threats + TOWS cross-strategies |
| `06-business-model.md` | Business Model & Revenue Streams | Revenue mix, engagement types, leverage model |
| `07-pricing-and-packaging.md` | Pricing & Packaging | Day rate, productized offers, retainer tiers, credit mechanics |
| `08-business-plan.md` | Business Plan | 11-section formal plan: exec summary, market, GTM, ops, financials, risks |

### 02 · Brand (8 pages)

| File | Title | Key contents |
| --- | --- | --- |
| `01-brand-strategy.md` | Brand Strategy | Brand idea, promise, pillars, personality, positioning vs competitors |
| `02-naming.md` | Naming | Core naming decision, recommendation, parking-lot alternatives, decision log |
| `03-visual-identity.md` | Visual Identity Direction | Color, type, layout principles, photography/illustration direction |
| `04-voice-and-tone.md` | Voice & Tone | Voice attributes, tone shifts by channel, never-list |
| `05-messaging.md` | Messaging & Core Copy | Message hierarchy, taglines, elevator pitches, value props, hero copy, bios, objection one-liners |
| `06-logo-concepts.md` | Logo Concepts | Concept directions, rationale, usage notes (may reference `media/`) |
| `07-voice-reference.md` | Voice Reference | Evidence-based voice doc from real writing: traits, vocabulary, templates, annotated examples, reusable voice prompt |
| `08-design-system.md` | Design System | Tokens, components, layout rules for all studio-owned surfaces |

### 03 · Offerings (5 pages)

| File | Title | Key contents |
| --- | --- | --- |
| `01-service-catalog.md` | Service Catalog | Full ladder of services with scope summaries |
| `02-wedge-offer-audit.md` | Wedge Offer | Productized audit: promise, price, deliverables, SOP, checklist, conversion mechanics (Mermaid funnel) |
| `03-retainers-and-packages.md` | Retainers & Packages | Fractional/retainer tiers, scope boundaries |
| `04-products-and-tooling.md` | Products & Tooling | Lead magnets, ebooks, plugins, digital products |
| `05-case-study-strategy.md` | Case Study Strategy | Which stories to tell, structure, permission/anonymization rules |

### 04 · Marketing (9 pages)

| File | Title | Key contents |
| --- | --- | --- |
| `01-marketing-strategy.md` | Marketing Strategy | Positioning-led GTM, reputation funnel, channel priorities |
| `02-content-engine.md` | Content Engine | Pillars, formats, cadence, repurposing rules |
| `03-channels.md` | Channels | LinkedIn, Instagram, newsletter, communities, speaking |
| `04-lead-generation.md` | Lead Generation | Inbound + outbound mix, lead magnets, CTAs |
| `05-website-plan.md` | Website & Portfolio Plan | Site structure, conversion checklist, gaps, priorities |
| `06-outreach-compliance.md` | B2B Outreach Compliance (Germany/EU) | UWG §7, GDPR, channel-specific rules |
| `07-outreach-plan.md` | Outreach Plan | Warm-first sequences, volume targets, cadence |
| `08-marketing-funnel.md` | Marketing Funnel | Awareness → consult → audit → build (Mermaid) |
| `09-outreach-compliance-international.md` | International Outreach | Non-DACH compliance notes |

### 05 · Sales (4 pages)

| File | Title | Key contents |
| --- | --- | --- |
| `01-sales-process.md` | Sales Process | Pipeline stages, qualification, timing |
| `02-proposals-and-sow.md` | Proposals & SOW | 3-option model, scope rules, legal hooks |
| `03-contracts.md` | Contracts & Agreements | MSA, SOW, NDA, DPA checklist |
| `04-onboarding.md` | Client Onboarding & Offboarding | Kickoff, access, communication norms, offboarding |

### 06 · Operations (4 pages)

| File | Title | Key contents |
| --- | --- | --- |
| `01-tools-and-stack.md` | Tools & Stack | CRM, booking, e-sign, accounting, design/dev tools |
| `02-delivery-workflow.md` | Delivery Workflow | End-to-end engagement flow |
| `03-sops.md` | SOPs & Templates | Standard operating procedures index |
| `04-quality-bar.md` | Quality Bar & Definition of Done | Deliverable standards, review checklist |

### 07 · Finance & Legal (5 pages)

| File | Title | Key contents |
| --- | --- | --- |
| `01-legal-setup-germany.md` | Legal Setup | Freiberufler vs Gewerbe, employer notification, VAT, insurance, setup checklist |
| `02-finance-model.md` | Finance Model | Revenue targets, cost structure, margin assumptions |
| `03-savings-and-cushion.md` | Savings & Runway | Side-venture runway, transition triggers |
| `04-templates.md` | Documents & Templates Checklist | Invoices, contracts, filings |
| `05-financial-projections.md` | Financial Projections | Year 1-3 scenarios |

> **Adaptation note:** Replace jurisdiction-specific legal/finance docs for the target business's country. Keep the same *structure* (setup checklist, finance model, runway, projections).

### 08 · Roadmap (4 pages)

| File | Title | Key contents |
| --- | --- | --- |
| `01-90-day-launch.md` | 90-Day Launch Plan | 3-month phased plan with checkboxes (foundation → launch → sell) |
| `02-transition-to-fulltime.md` | Transition to Full-Time | 6- and 12-month triggers, financial gates |
| `03-milestones-and-kpis.md` | Milestones & KPIs | Measurable success criteria by phase |
| `04-task-backlog.md` | Master Task Backlog | Consolidated checkbox list linking to all other docs |

### 09 · Toolkit (16 pages) - execution layer

| File | Title | Asset type | Volume |
| --- | --- | --- | --- |
| `00-toolkit-index.md` | Toolkit Index | Navigation + usage rules | - |
| `01-outreach-playbook.md` | Outreach Playbook | Warm intro, LinkedIn, phone, email templates | Multi-channel scripts |
| `02-linkedin-launch-posts.md` | LinkedIn Launch Posts | Full post copy | **12 posts** |
| `03-content-calendar.md` | Content Calendar | 90-day posting plan | 3×/week LinkedIn + monthly newsletter |
| `04-proposal-template.md` | Proposal Template | 3-option client proposal | Fill-in sections with `{{placeholders}}` |
| `05-sow-template.md` | SOW Template | Statement of work | Scope, milestones, terms |
| `06-audit-report-template.md` | Audit Report Template | Client deliverable skeleton | Executive summary, findings, roadmap |
| `07-invoice-template.md` | Invoice Template | German-compliant invoice | Line items, VAT, legal fields |
| `08-client-emails.md` | Client Emails | Onboarding, follow-up, testimonial asks | ~10 email templates |
| `09-discovery-call-script.md` | Discovery Call Script | 30-min consult structure | Questions, listen-fors, close |
| `10-linkedin-posts-proof.md` | LinkedIn Proof Batch | Authority/inbound posts | **12 posts** |
| `11-instagram-posts-stories.md` | Instagram Posts & Stories | Feed + Story copy | **14 feed + 14 stories** |
| `12-instagram-figma-agentic-workflows.md` | Instagram Agentic Workflows | Niche topic batch | **10 posts + 10 stories** + LinkedIn adaptations |
| `13-agentic-design-engineering-28-series.md` | 28-Post Series | Dual-channel content series | **28 posts** + 14-week calendar + repurpose pipeline |
| `13-agentic-design-engineering-28-visual-strategy.md` | 28-Post Visual Strategy | Carousel/Reel art direction | Per-post visual specs |
| `14-design-dev-collaboration-social.md` | Collaboration Social Pack | LinkedIn + Instagram for one lead magnet | **10 LI + 8 IG** |

**Toolkit content totals (approximate):**

| Channel | Ready drafts |
| --- | --- |
| LinkedIn | 12 launch + 12 proof + 10 collaboration + 28 series + bonus adaptations ≈ **60+** |
| Instagram | 14 + 14 stories + 10 + 10 stories + 8 collaboration + 28 series adaptable ≈ **80+ pieces** |
| Sales/delivery | Proposal, SOW, audit report, invoice, discovery script, ~10 emails |
| Outreach | Warm intro, LinkedIn DM sequences, phone script, consent-gated email |

---

## 4. Agent skills layer (build in parallel with docs)

Skills live in `agents/skills/` as folders with `SKILL.md` (YAML frontmatter + markdown). They are the **quality and consistency engine** when an agent generates new copy.

### Required core skills

| Skill | Purpose |
| --- | --- |
| `studio-profile` | Canonical facts: bio, proof points, ICP, offers, pricing. **Single source of truth for numbers.** |
| `studio-voice` | Voice, tone, signature phrases, never-list, quick check. Includes `humanizer-patterns.md` for anti-AI pass. |

### Channel / deliverable skills (layer on top)

| Skill | Purpose |
| --- | --- |
| `linkedin-posts` | Hooks, archetypes, post structure |
| `instagram-posts` | Feed, Reels, Stories formats |
| `dach-b2b-outreach` | Compliant outreach scripts (adapt jurisdiction) |
| `client-proposals` | 3-option proposals + SOW + pricing |
| `design-system-audit` | Audit methodology + report structure |
| `discovery-calls` | Consult flow + qualification + close |
| `case-studies` | Story-led proof documents |
| `design-system` | Visual token rules for UI/copy surfaces |
| `book-knowledge-base` | Optional: extract long-form books into KB chapters |

### IDE enforcement

Create `.cursor/rules/voice.mdc` (or equivalent) with `alwaysApply: true`:

1. Read `studio-voice` + `humanizer-patterns` before any user-facing text
2. Read `studio-profile` - no invented facts or numbers
3. Layer the matching channel skill
4. Draft → humanize pass → self-check

Symlink skills for auto-discovery:

```bash
mkdir -p .cursor && ln -s ../agents/skills .cursor/skills
```

---

## 5. Visual / UI specification for `site/`

The HTML suite uses a **documentation chrome** skinned with the business's design tokens:

| Element | Spec |
| --- | --- |
| Layout | Fixed 300px sidebar + fluid content; max prose width ~760px |
| Typography | Inter (UI + prose), JetBrains Mono (code) |
| Colors | Imported from `website/design-system/tokens.css` - indigo primary, neutral surfaces |
| Dark mode | `.dark` class on `<html>`; toggled via button; respects `prefers-color-scheme` initially |
| Components | `.prose`, `.toc`, `.cards` / `.card`, `.sidebar`, blockquotes, code blocks |
| Motion | `motion.css` - micro transitions; respects `prefers-reduced-motion` |
| Diagrams | Mermaid flowcharts in strategy, offerings, marketing, overview |
| Footer | "Generated from Markdown · node build.mjs · [Business name] business suite" |

Source CSS: `assets/styles.css` (hand-maintained, copied to `site/assets/` at build).

---

## 6. Agent build order (recommended phases)

Use this sequence for another business. Each phase ends with **shippable artifacts**, not endless strategy.

### Phase 0 - Scaffold (Day 1)

- [ ] Create repo layout (`docs/`, `agents/skills/`, `assets/`, `build.mjs`, `package.json`)
- [ ] Port or write `build.mjs` and verify empty build works
- [ ] Create minimal `assets/styles.css` + token imports
- [ ] Create `studio-profile` skill with **real** facts only (bio, offers, pricing placeholders marked TBD)
- [ ] Create `studio-voice` skill from founder's existing writing samples

### Phase 1 - Foundation docs (Week 1)

Build in dependency order:

1. `00-overview.md` - thesis, north star, operating principles, section map
2. `01-strategy/` - all 8 files (positioning and ICP are critical path)
3. `02-brand/` - at minimum: brand strategy, voice, messaging, voice reference
4. `03-offerings/` - service catalog + **one wedge offer** fully productized

**Exit criteria:** A stranger can read overview + strategy + wedge offer and understand what the business sells, to whom, and why it's credible.

### Phase 2 - Go-to-market docs (Week 2)

5. `04-marketing/` - strategy, content engine, channels, funnel, outreach plan
6. `05-sales/` - process, proposals, contracts outline, onboarding
7. `08-roadmap/` - 90-day plan + master task backlog (pulls checkboxes from everywhere)

**Exit criteria:** 90-day launch plan is executable; backlog has 50+ concrete checkboxes.

### Phase 3 - Operations & finance (Week 2-3)

8. `06-operations/` - tools, workflow, SOPs, quality bar
9. `07-finance-legal/` - jurisdiction-specific setup ( **not** generic placeholders)

**Exit criteria:** Founder knows legal next steps, target rates, and runway math.

### Phase 4 - Toolkit burst (Week 3-4)

10. `09-toolkit/` index + sales templates (proposal, SOW, discovery script, emails)
11. Wedge deliverable template (audit report or equivalent)
12. Outreach playbook
13. **Social content batches** - minimum viable:
    - 12 launch LinkedIn posts
    - 12 proof/authority LinkedIn posts
    - 90-day content calendar
    - One Instagram batch (10-14 posts) if visual channel matters

**Exit criteria:** Founder can run a discovery call, send a proposal, and publish 4 weeks of content without writing from scratch.

### Phase 5 - Depth & series (Week 4+)

14. Long-form content series (e.g. 28-post interleaved calendar)
15. Visual strategy doc for carousels/Reels
16. Topic-specific social packs tied to lead magnets
17. Remaining brand docs (logo concepts, full design system)
18. `AGENT-PLAYBOOK.md` - agent task ideas for ongoing extension

**Exit criteria:** 90+ days of content exists; sales assets cover full funnel.

### Phase 6 - Polish & wire

- [ ] Run `npm run build`; fix broken internal links
- [ ] Add Mermaid diagrams to overview, wedge offer, funnel
- [ ] Symlink skills; add Cursor rule
- [ ] Optional: public `website/` for lead gen (separate from internal suite)

---

## 7. Per-document content patterns (what "good" looks like)

Agents should match these patterns when creating equivalent docs for another business.

### Strategy docs

- Open with **one sharp claim**, not background fluff
- Include **tables** for comparisons (competitors, pricing tiers, ICP segments)
- End with **"so what" takeaways** that link forward to offerings or marketing
- Use **Mermaid** for models with more than 3 steps

### Brand docs

- `05-messaging.md` must have **ready-to-paste** copy blocks: hero, bios (50/100/150 word), taglines, objection handlers
- `07-voice-reference.md` must cite **real founder writing**, not invented examples
- Never-list and quick-check in voice skill must stay in sync

### Wedge offer doc

- Mermaid: Lead → consult → paid wedge → upsell
- Fixed **price range**, **duration**, **deliverable list**
- Repeatable **delivery SOP** (numbered steps)
- **Starter checklist** the consultant runs every time
- **Productization assets** checklist (what templates to build)

### Toolkit templates

- Use `{{placeholder}}` syntax for personalization
- Include **usage tips** section at bottom
- Cross-link to voice, compliance, and messaging docs
- Social posts: each post in a `blockquote` or clearly delimited block; note format (carousel, story frames, reel script)

### Roadmap docs

- Checkbox syntax `- [ ]` throughout
- Link every task to the deep doc: `([audit](../03-offerings/02-wedge-offer-audit.md))`
- Phases with **explicit success metrics** at day 90 / month 6 / month 12

---

## 8. Adaptation checklist for a new business

Replace these elements; keep the structure.

| Element | Action |
| --- | --- |
| Business name / founder | Throughout README, sidebar brand, skills, messaging |
| Thesis & wedge | Rewrite `00-overview`, positioning, wedge offer for new niche |
| ICP & market | New segments, competitors, day rates for their geography |
| Proof points | **Only real metrics and clients** in profile skill and posts |
| Pricing | Local currency, local market rates, local tax treatment |
| Legal/finance | New country docs (don't copy German Freiberufler content blindly) |
| Outreach compliance | Jurisdiction-specific rules |
| Wedge deliverable | Rename audit → whatever their entry offer is (assessment, sprint, workshop) |
| Social content | Rewrite all posts; keep archetypes (launch, proof, framework, lead magnet, hot take) |
| Design tokens | Re-skin CSS from new brand palette |
| Public website link | Sidebar `suite-site-link` href |
| Invoice template | Local legal requirements |

**Do not copy:**

- Specific client names unless public and permitted
- Nord Security / Aurora references
- German tax/legal specifics into non-German businesses without rewrite
- Metrics (90% reclamation, etc.) unless the new founder has equivalent proof

---

## 9. Quality bar - what makes it "extensive"

The suite is considered complete at v1 when all of the following are true:

### Coverage

- [ ] Every function of a solo consultancy has a home doc (strategy → cash collection)
- [ ] At least one **productized wedge offer** is fully specified end-to-end
- [ ] Master backlog consolidates tasks from all sections
- [ ] Toolkit separates **strategy** (sections 01-08) from **execution** (section 09)

### Content depth

- [ ] ~6,000+ lines of Markdown across 60+ files
- [ ] 90+ social posts drafted (not outlines - full copy)
- [ ] 8+ fill-in templates (proposal, SOW, report, emails, invoice, discovery script, outreach)
- [ ] Voice reference grounded in real writing samples
- [ ] 90-day calendar maps posts to weeks

### Agent-readiness

- [ ] `studio-profile` skill has all facts agents must not invent
- [ ] `studio-voice` skill has never-list + humanizer patterns
- [ ] Channel skills exist for primary GTM motions
- [ ] Cursor rule enforces skill workflow
- [ ] Internal links between docs form a graph (overview → strategy → offerings → toolkit)

### Human usability

- [ ] `npm run build` produces browsable HTML with nav, TOC, dark mode
- [ ] Dashboard cards give section overview at a glance
- [ ] Mermaid diagrams render in browser
- [ ] Mobile sidebar works

### Business usability

- [ ] Founder can execute Month 1 of 90-day plan using only these docs
- [ ] First proposal sendable with template + skill only
- [ ] First month of LinkedIn schedulable from toolkit without new writing

---

## 10. Prompt template for the replication agent

Paste and customize:

```
You are building a complete Business Suite for [FOUNDER NAME]'s [BUSINESS TYPE] 
consultancy, modeled on the Design Engineering Studio suite architecture.

Read SITE-BUSINESS-SUITE-REPLICATION-PLAN.md in full before starting.

Constraints:
- Markdown in docs/ is source of truth; site/ is generated via build.mjs
- Create agents/skills/studio-profile and studio-voice FIRST with real facts only
- Follow numbered section order: overview → strategy → brand → offerings → 
  marketing → sales → operations → finance → roadmap → toolkit
- Section 09 toolkit must contain full copy, not bullet outlines
- Minimum social content: 12 launch LinkedIn + 12 proof LinkedIn + 90-day calendar
- One fully productized wedge offer with SOP, checklist, and report template
- Jurisdiction: [COUNTRY] for legal/finance/invoice/compliance docs
- Wedge offer: [OFFER NAME] at [PRICE RANGE]
- ICP: [PRIMARY CLIENT DESCRIPTION]

Phase 1 deliverable: docs/00-overview.md through docs/03-offerings/ complete.
Run npm run build and fix any broken links.

Do not invent proof points, client names, or metrics. Mark unknowns as TBD in studio-profile.
```

---

## 11. Related assets outside `site/` (optional extensions)

The Design Engineering Studio repo extends beyond the internal suite. A full clone for another business may eventually add:

| Asset | Location | Purpose |
| --- | --- | --- |
| Public marketing site | `website/` | Lead gen, ebooks, health check quiz, blog |
| Agent playbook | `AGENT-PLAYBOOK.md` | 40+ agent task ideas with prompts |
| Ebooks | `website/*-ebook.html` | PDF-ready lead magnets |
| Blog generator | `website/blog/generate-posts.mjs` | HTML posts from content seeds |
| Social series pages | `website/social-series/` | Styled post previews |
| Remotion pipeline | `animated-posts/` | Video/Reel generation |
| Design system graphics | `design-system-graphics/` | SVG library for carousels |

These are **not required** for the core business suite but demonstrate how the toolkit content propagates to public channels.

---

## 12. File count summary

| Category | Count |
| --- | --- |
| Markdown source files (`docs/`) | 64 |
| Generated HTML pages (`site/`) | 65 (64 + dashboard) |
| CSS/assets (hand-maintained) | 3 (`styles.css`, `tokens.css`, `motion.css`) |
| Agent skills | 11 |
| Numbered sections | 9 (+ Start) |
| Toolkit execution docs | 16 |
| Approx. total Markdown lines | ~6,900 |
| Approx. ready social post drafts | 90+ |

---

## 13. Maintenance workflow

1. **Edit** `docs/**/*.md` (or ask agent to, with skills loaded)
2. **Run** `npm run build`
3. **Review** in browser at `site/index.html`
4. **Update** `studio-profile` skill when pricing/offers/facts change
5. **Extend** toolkit by adding numbered files (`15-new-pack.md`) and rebuilding
6. **Track** execution in `08-roadmap/04-task-backlog.md`

Never hand-edit `site/` HTML - it is wiped on every build.

---

*This inventory describes the Design Engineering Studio Business Suite as of June 2026. Use it as a blueprint; adapt every fact, law, and proof point to the target business.*
