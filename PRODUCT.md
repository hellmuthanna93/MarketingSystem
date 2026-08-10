# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary users of the public practice site are sensitive, thoughtful adults who already understand a lot about themselves and still feel stuck. Many are international or in life/career transition; sessions may be in English, German, Ukrainian, Russian, or a mix.

Their job on the site is to decide whether Anna is the right support and take the next step: schedule a free 30-minute discovery call.

Secondary users of this MarketingSystem repo are Anna (and agents) producing brand-consistent marketing, internal business-suite materials, and client-facing deliverables. Those surfaces share brand, voice, and practice facts; they are not the visitor conversion surface.

## Product Purpose

MarketingSystem is the durable brand and marketing foundation for Anna Hellmuth Psychological Counseling and Life Coaching. It exists so every public and internal surface stays consistent with practice truth, voice, and visual identity.

The public product surface is [annahellmuth.com](https://annahellmuth.com/): an online, location-independent practice offering psychological counseling and The Next Chapter life-coaching program.

**Success (public site):** a right-fit visitor books a discovery call.

## Positioning

Help people create lasting inner change. Combine psychological depth with coaching practicality so clients both understand themselves and move forward. Sell movement (relief, clarity, possibility), not process, method, or session mechanics. Neighboring coaches who only motivate, or therapists who only explain, cannot truthfully claim this combination.

## Operating Context

- Public multilingual static site (`website/anna-hellmuth/`, locales EN / DE / UK / RU) built from Jinja sources; preview via local static server; live at annahellmuth.com
- Shared brand system in `brand/` (tokens, typography, components, voice, marketing docs)
- Internal business suite (`business-site/`) for operating manuals and delivery workflows
- Styleguide and design-system HTML for visual reference and components
- Discovery call booking: Google Calendar link (canonical in practice-profile)
- Online sessions; office Impressum address in Nuremberg, Germany

## Capabilities and Constraints

**Capabilities (confirmed):**

- Public pages for counseling, life coaching (The Next Chapter), about, contact, blog, support quiz, legal (impressum / privacy)
- Multilingual site with hreflang and language switcher
- Free 30-minute discovery call as the primary entry offer
- Psychological counseling packages and The Next Chapter coaching offer (facts only from practice-profile)
- Soft primary CTA: Schedule your discovery call

**Constraints:**

- Never invent pricing, credentials, metrics, testimonials, client identity, or outcome guarantees; unknowns are TBD
- Do not hardcode brand hex in `projects/` or `website/`; edit palette only in `brand/tokens.css`
- DACH mental-health / Beratung compliance for health claims, scope, outreach, and testimonials
- Clarity Session wedge: proposed, not live; do not publish until approved
- `projects/table/` still uses a legacy palette (Phase 2 realign); not canonical website brand
- Stack is existing static HTML/CSS (Jinja build for the public site); not a framework SPA

**Undecided / out of scope for this record:** aesthetic redesign direction (owned by design work, not PRODUCT.md).

## Brand Commitments

- **Name:** Anna Hellmuth · practice name Anna Hellmuth Psychological Counseling and Life Coaching
- **Voice:** warm, confident, precise about stuck patterns; sell movement; soft CTAs; no motivational slogans, pity, or credential flexing (see `brand/voice.md` and practice-voice skill)
- **Visual identity authority for refinement:** incumbent burgundy/cream system and Source Serif 4 in `brand/` (DESIGN.md at `brand/DESIGN.md`); redesign must treat replacement of that world as an explicit new-work decision, not silent drift
- **Assets and copy sources:** `brand/`, practice-profile skill, approved messaging in `brand/marketing/`

## Evidence on Hand

- Live site: https://annahellmuth.com/
- Practice facts: `.cursor/skills/practice-profile/SKILL.md`
- Positioning, messaging, sales: `brand/marketing/`
- Voice: `brand/voice.md`
- Visual tokens and components: `brand/tokens.css`, `brand/DESIGN.md`, `styleguide/`, `design-system/`
- Site source: `website/anna-hellmuth/src/`
- Business suite: `business-site/`

**Do not fabricate:** client names or identifying detail; numeric outcome claims; unpublished testimonials; insurance reimbursement claims; new prices or packages.

## Product Principles

1. Right-fit over volume: the site and marketing should attract people who belong here and let others self-select out.
2. Movement over method: communicate change and possibility, not process theater.
3. Practice truth only: every factual claim traces to practice-profile or Anna’s confirmation.
4. One brand system: public site, marketing assets, and internal suite share tokens, voice, and constraints.
5. Soft invitation: primary action is a discovery call, never hard-sell or guaranteed outcomes.

## Accessibility & Inclusion

Multilingual access (EN / DE / UK / RU) is a product requirement. No separate formal accessibility standard was established beyond ordinary web good practice for a marketing site; raise WCAG target only if Anna sets one later.
