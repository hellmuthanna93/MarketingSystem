# Website & Portfolio Plan

The public site ([Website/anna-hellmuth/](../../../Website/anna-hellmuth/), live at annahellmuth.com) is the conversion hub. This doc audits it against the funnel and lists priorities. The site **mirror** in this repo reflects the live structure.

## Current structure (live)

| Page | Role |
|------|------|
| index.html | Hero, services intro, transformation, CTA |
| counseling.html | Counseling lane - H1 "You don't have to face this alone" |
| lifecoaching.html | Coaching lane - H1 "You need a courageous heart…" |
| about.html | Trust, credentials, origin story |
| contact.html | Contact + discovery call |
| blog/ | Compounding content (burnout, counseling-vs-coaching, expat, signs-you-need-support) |
| impressum.html / privacy-policy.html | Legal |

## Conversion checklist

- [x] Remove the retired coaching offers and replace them with The Next Chapter
  (€1,950). English source copy is live in the build; full DE, UK, and RU body
  translation is still required.
- [ ] Discovery call CTA visible on every page (nav + footer + in-content)
- [ ] Counseling vs coaching self-selection is obvious within one scroll
- [ ] Movement-first hero copy (note: legacy hero/footer still say "creative & ambitious souls" - prefer "sensitive, thoughtful souls" in new copy)
- [ ] Testimonials present, anonymous, with privacy note
- [x] Multilingual entry/affordance (EN / DE / UK / RU) clear
- [ ] Blog posts link to service pages + discovery call
- [ ] Trust signals (credentials, directory badge) on about/service pages, not hero
- [ ] Fast, mobile-clean, accessible (skip links present in current build)

## Gaps & opportunities

| Gap | Priority | Note |
|-----|----------|------|
| **Clarity Session wedge page** | High (after Anna confirms) | New offer needs a page; render draft in [../../render/03-offerings-02-wedge-clarity-session.html](../../render/03-offerings-02-wedge-clarity-session.html) |
| Newsletter signup | Medium | Owned audience; double opt-in |
| Lead magnet | Medium | Pattern self-assessment |
| Multilingual content depth | Medium | More DE / UK / RU pages or content |
| Hero copy update | Low | Align to "sensitive, thoughtful souls" |
| More anonymized pattern stories | Low | Trust without exposure |

## Priorities (sequenced)

1. Keep discovery-call CTA frictionless everywhere
2. Add the wedge page once the offer is confirmed
3. Add newsletter capture + a first lead magnet
4. Deepen multilingual content
5. Refresh hero/footer label

## Rules

- All pages link `brand/tokens.css` + `typography.css` + `components.css` (no hardcoded hex)
- Re-scrape/refresh mirror via `python3 website/scripts/build-website.py` only when syncing from live
- Don't hand-edit generated mirror as if it were source unless intentionally updating the mirror

## So what

The site is solid and on-brand; the main funnel gap is the **wedge page** plus **owned-audience capture** (newsletter + lead magnet). Sequenced into the roadmap ([../08-roadmap/01-90-day-launch.md](../08-roadmap/01-90-day-launch.md)).
