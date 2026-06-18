# Design Review & Improvement Plan — annahellmuth.com

Prepared as a **proposal for review**. Nothing here is applied to the live site yet. Each item is rated by priority and tied to a concrete business reason, so we can pick what to work on together.

Companion file: open **`design-review/index.html`** in a browser for the visual before/after examples.

---

## 1. The business this design has to serve

Pulled from `brand/marketing/` and `brand/voice.md` so every recommendation ladders up to a real goal:

| Driver | What it means for the site |
|--------|----------------------------|
| **One conversion: the free discovery call** | Every page exists to move the right person to "Schedule your discovery call." This is the single metric the design should optimize. |
| **Premium, low-volume practice** (€300k goal, high-quality clients, not high-volume) | The site must *feel* expensive and trustworthy. Polish, calm, and credibility matter more than aggressive funneling. |
| **Trust is the #1 lever** (trust → visibility → consistency → depth) | "Finally, someone understands what I'm experiencing." The design's job is to make a sensitive, discerning reader feel understood and safe. |
| **Sell movement, not process** | Lead with relief / clarity / transformation. Credentials and methods support trust but never shout. |
| **Audience: sensitive, self-aware professionals 25–45**, often expat / Ukrainian / Russian / German, multilingual | Calm feminine aesthetic, no hype, no pressure. Multilingual reach is a real, underused advantage. |
| **No-pressure sales** ("Why not give it a try and find out?") | Reassurance is welcome; urgency / scarcity tactics are off-brand and must be avoided. |

**Design read:** A multi-page service/marketing site for a premium online psychological-counseling & life-coaching practice, for sensitive high-functioning adults, with a warm editorial language, on an established brand (burgundy `#64010d` + cream + Source Serif 4), hand-coded static HTML/CSS. This is a **Redesign – Preserve**: evolve and tighten, do not re-skin.

**Dials (matched to the existing brand, not the skill's aggressive baseline):** `DESIGN_VARIANCE 6 · MOTION 4 · DENSITY 3`.

---

## 2. Scorecard (current state)

| Page | Conversion | Trust | Clarity | Visual polish | Notes |
|------|:---------:|:-----:|:-------:|:-------------:|-------|
| Home | ◑ | ● | ◑ | ● | Strong brand; CTA repeated 4×, testimonials wall is heavy, hero runs long |
| Counseling | ◑ | ● | ● | ● | Good; CTA labels drift ("Book a free 30 min session", "Let's discuss the plan") |
| Life coaching | ○ | ◑ | ○ | ◑ | **Contains broken/placeholder copy**; different hero pattern; CTA label + destination drift |
| About | ● | ● | ◑ | ● | Rich and credible; very long; education/credentials could work harder as trust signals |
| Contact | ◑ | ● | ● | ◑ | Clean; the booking embed is the real CTA but competes with email-first copy |
| Blog | ● | ◑ | ● | ● | Best-structured template on the site; good model for the rest |
| Legal (Impressum / Privacy) | – | ● | ● | ● | Fine |

● solid · ◑ needs work · ○ problem

**Headline takeaway:** the brand and craft are genuinely good. The gap is **conversion consistency** and **a few credibility leaks** (broken copy, drifting CTAs), not a visual overhaul. The highest ROI is tightening what already exists.

---

## 3. Prioritized roadmap

Priority = business impact × confidence. Effort is rough (S < half day, M ~1 day, L multi-day).

### P0 — Do first (credibility + the one conversion)

| # | Item | Why it matters to the business | Effort |
|---|------|-------------------------------|:------:|
| 1 | **Fix broken copy on Life Coaching** ("Say it to be delightful are my momma…" and surrounding garbled text) | A premium practice cannot ship gibberish on a money page. Instantly erodes the trust the whole model depends on. | S |
| 2 | **Standardize the primary CTA label** to one phrase everywhere: **"Schedule your discovery call"** (canonical in `voice.md`/`sales.md`). Retire "Book a discovery call", "Book a free 30 min session with me", "Let's discuss the plan". | One clear action = higher conversion and a more confident brand. Mixed labels read as inconsistency. | S |
| 3 | **Unify CTA destination & behavior.** Today: home hero → `#intake`, nav → external Google Calendar (new tab), life-coaching hero → `contact.html`. Pick one model (recommended: every primary CTA lands on the embedded scheduler). | Predictable booking path removes friction at the exact moment of intent. New-tab hand-offs lose people. | M |
| 4 | **Add quiet reassurance microcopy** under primary CTAs: "Free · 30 minutes · no obligation." (reassurance, not pressure) | Lowers hesitation for a cautious audience without violating the no-pressure rule. | S |

### P1 — High value (trust, self-selection, scannability)

| # | Item | Why it matters | Effort |
|---|------|----------------|:------:|
| 5 | **Curate the testimonials** into a tight, scannable set (lead with the bolded one-line transformation; full quote behind "read more" or a carousel). Cap visible quote to ~3 lines. | The current wall of long quotes is skimmed, not read. Curation reads as more premium and confident. | M |
| 6 | **Add a compact, calm trust strip** (qualifications: MD + psychologist + hypnotherapy in training; online since 2023; 4 languages; Location Independent Therapists). Surfaced on home + service pages, factual not boastful. | Premium positioning needs visible credibility; right now it's buried on About. | M |
| 7 | **Add a "Counseling vs Coaching" chooser** block on the home and/or a shared section (the comparison already exists in `audience.md`). | The "which is right for me?" fork is a core conversion decision; helping the right client self-select fast increases qualified bookings. | M |
| 8 | **Tighten the home hero** so value prop + one CTA are visible in the first viewport; move the long reflective paragraphs into the section below. | First impression decides whether a sensitive reader stays. The CTA shouldn't require scrolling past 4 paragraphs. | M |
| 9 | **Unify the hero system** across pages (home / counseling / coaching / contact currently use 4 different patterns). | Consistency = perceived quality and easier maintenance. | M |
| 10 | **SEO & sharing:** add `ProfessionalService` + `Person` structured data, Open Graph / Twitter cards, canonical tags. | A discovery-led practice lives on being found and shared credibly. Low effort, compounding return. | M |

### P2 — Polish & strategic (do after the above)

| # | Item | Why it matters | Effort |
|---|------|----------------|:------:|
| 11 | **Multilingual plan:** at minimum signal "sessions in your language" as a trust element; ideally localized DE / UK / RU landing pages with `hreflang`. | The ideal client is frequently Ukrainian/Russian/German. Meeting them in their language is a major, underused advantage. | L |
| 12 | **Reading comfort for long pages:** constrain body measure to ~65ch, break long text runs with subheads / pull quotes / imagery; vary section layout families to avoid monotony (esp. life coaching). | Sensitive, deep readers still skim online; rhythm keeps them moving toward the CTA. | M |
| 13 | **Move inline styles into component classes** in `brand/components.css` / site CSS. | The pages are full of inline styles; consolidating makes future iteration faster and more consistent. | L |
| 14 | **Public-label decision:** hero says "creative & ambitious souls"; strategy prefers "sensitive, thoughtful souls." Decide and apply consistently. | Positioning precision = sharper self-recognition by the right client. (Copy decision, needs your sign-off.) | S |
| 15 | **Imagery consistency:** ensure warm, premium, feminine photography across pages; consistent treatment and aspect ratios. | Photography carries the "premium + warm" feeling more than any CSS. | M |

---

## 4. Detailed findings by theme

### 4.1 Conversion architecture (the discovery call)
- **Label drift** across pages: `Schedule your discovery call` (nav/home), `Book a discovery call` (coaching hero), `Book a free 30 min session with me` and `Let's discuss the plan` (counseling). → One primary label.
- **Destination drift:** in-page anchor vs external new-tab vs contact page. → One predictable path; prefer the embedded scheduler so intent converts in place.
- **Repetition without variation:** home repeats the identical CTA 4× in the body. Keep CTAs at natural decision points (after hero, after services, after testimonials, at the scheduler) but let the surrounding context do the persuading, not a fourth identical button.
- **Missing reassurance:** no "free · 30 min · no obligation" near buttons. A cautious audience benefits from this; it's reassurance, not urgency.
- **Secondary CTAs** ("Discover Counseling Services" / "Explore Coaching Details") are good and distinct — keep them, just unify wording style.

### 4.2 Trust & premium positioning
- Credentials (MD; psychologist & coach; hypnotherapy in training; online since 2023) live only deep in About. A **calm credentials strip** on home + service pages would do real work — kept factual to respect the "don't show off" voice rule.
- The **Location Independent Therapists** badge and multilingual capability are trust assets that are currently quiet. Surface them.
- Testimonials are anonymized with a privacy note — correct and on-brand. The issue is **volume and length**, not authenticity.

### 4.3 Content & clarity
- **Life coaching broken copy** (P0 #1): the "Do I really need a coach?" intro contains corrupted, non-grammatical text. Rewrite using `messaging.md` voice (movement-first, warm, grounded).
- **Counseling vs coaching** is the reader's central question and is currently only answered inside an FAQ accordion. Promote it to a visible, visual chooser (table/cards) — the content already exists in `audience.md`.
- **Public label** ("creative & ambitious souls" vs "sensitive, thoughtful souls") — align per strategy once you decide.

### 4.4 Layout, hierarchy & visual system
- **Hero runs long** on home (H1 + subhero + divider + image + 4 paragraphs + CTA + more text + CTA) — the primary action sits well below the fold.
- **Four different hero patterns** across pages reduce cohesion. Define one hero system with variants.
- **Section monotony** on life coaching (many full-width centered text blocks in a row). Vary layout families and insert visual breaks.
- **Heavy serif body** at generous measures is beautiful but tiring in long runs — constrain measure and add rhythm. (Keep Source Serif 4; this is brand.)

### 4.5 Accessibility & technical (continues last round's dark-mode + a11y work)
- Footer copyright year is inconsistent (2025 on home, 2026 elsewhere).
- Client-avatar `alt="Client Avatar"` is generic; decorative avatars can use empty `alt`.
- `lang="en"` only; no `hreflang` — relevant once multilingual pages exist.
- Add structured data, OG/Twitter cards, canonical (SEO/sharing).
- Booking is a heavy third-party iframe (already lazy-loaded — good); keep an eye on it for performance.

### 4.6 What's already strong (preserve)
- The burgundy + cream + Source Serif 4 brand is distinctive and warm — keep it.
- Light/dark theming, reduced-motion, skip links, focus styles (from the last round) — keep.
- The **blog template** is the cleanest structure on the site; use it as the quality bar for other pages.
- Warmth of voice and the anonymized-testimonial integrity.

---

## 5. Suggested phasing

- **Phase 1 (credibility + conversion, ~1–2 days):** P0 #1–4. Fix copy, unify CTA label + destination, add reassurance microcopy.
- **Phase 2 (trust + self-selection, ~3–4 days):** P1 #5–10. Testimonial curation, trust strip, counseling-vs-coaching chooser, hero tighten + unify, SEO.
- **Phase 3 (scale + polish, ongoing):** P2 #11–15. Multilingual, reading comfort, CSS consolidation, label decision, imagery.

Start with Phase 1 — it's small, removes the credibility leaks, and directly serves the one conversion.

---

## 6. Open questions for you

1. **Booking model:** keep the embedded Google Calendar as the single destination, or do you want a lightweight intermediate "before we talk" step?
2. **Public label:** stay with "creative & ambitious souls," or move to "sensitive, thoughtful souls" per strategy?
3. **Multilingual:** is DE / UK / RU localization in scope this year, or just signal it for now?
4. **Copy latitude:** in the next working session, may I propose rewritten copy (life coaching especially), or keep edits visual-only?

> Visual before/after examples for items #1–8 are in `design-review/index.html`.
