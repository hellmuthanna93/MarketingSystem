---
target: Life coaching page
total_score: 23
max_score: 28
na_heuristics: 7,9,10
p0_count: 0
p1_count: 3
timestamp: 2026-08-24T11-54-32Z
slug: ellmuth-src-locales-en-bodies-lifecoaching-html-j2
---
## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|---|---:|---|
| 1 | Visibility of System Status | 3 | Expandable panels communicate their state, but the motion treatment on informational list rows can resemble a control. |
| 2 | Match Between System and Real World | 4 | Language accurately recognizes thoughtful, self-reliant people in transition. |
| 3 | User Control and Freedom | 3 | Discovery call is explicitly non-binding; the booking CTA competes with it for new visitors. |
| 4 | Consistency and Standards | 3 | Palette, typography, and controls are coherent; card and animation treatments are more varied than necessary. |
| 5 | Error Prevention | 3 | FAQs reduce wrong-fit risk, but the coaching/job-search boundary comes too late. |
| 6 | Recognition Rather Than Recall | 4 | Scope, process, outcomes, facts, and FAQs make the offer legible without memory burden. |
| 7 | Flexibility and Efficiency | n/a | Persuade surface; fast paths to scope/price are still an opportunity. |
| 8 | Aesthetic and Minimalist Design | 3 | Refined sections, but repeated proof and several interaction patterns lengthen the argument. |
| 9 | Error Recovery | n/a | No error-prone task occurs on this page. |
| 10 | Help and Documentation | n/a | FAQ and discovery call support the decision; conventional documentation does not apply. |
| **Total** | | **23/28** | **Strong foundation; simplify the conversion journey.** |

## Design Specificity Verdict

The page feels authored for Anna's practice rather than a generic coaching template. The burgundy-and-cream editorial system, quiet photography, language of meaningful transition, and gentle discovery-call invitation make a coherent, mature offer. The main opportunity is not a new visual identity; it is editing the experience so this distinctive voice lands with less repetition and fewer competing interaction patterns.

The automated scan found four low-severity items in `lifecoaching.html.j2`: an Arial checkmark glyph and two type-ramp advisories. The Arial finding is a false-positive design concern because it exists only for the circular checkmark glyph, not page typography. No console errors or horizontal overflow appeared at desktop or mobile widths. Mobile language links are smaller than ideal touch targets.

## Overall Impression

The page is warm, credible, and emotionally intelligent. It clearly understands the visitor before it invites a decision. Its biggest weakness is that it keeps making the same persuasive point after it has already earned it, which can make a self-reliant visitor feel guided through a funnel rather than respected as someone ready to evaluate the facts.

## What's Working

1. **The emotional opening respects competence.** It describes being capable, informed, and still stuck without pathologising the visitor. That is exactly the right psychological posture for this audience.
2. **The sequence itself is sound.** Recognition → why insight alone is insufficient → supported process → concrete method → outcomes → personal authority → offer is an understandable path from uncertainty to agency.
3. **Trust is multi-layered.** The lived-change story, portrait, programme facts, price, FAQ, and non-binding call each resolve a different kind of uncertainty. The resulting confidence feels earned rather than asserted.

## Priority Issues

### [P1] Repeated diagnosis slows the visitor before the solution

**Why it matters:** The transition, why-struggling list, and information section each state a version of the same point: insight/information alone does not create change. Repetition can exhaust an already thoughtful visitor and makes the page feel longer than its promise needs to be.

**Fix:** Retain the strongest articulation in the *Why does struggling alone…* and *More information…* sections. Reduce the preceding transition to a short visual pause or one bridging sentence, then move directly to the process.

**Suggested command:** `$impeccable distill`

### [P1] The key fit boundary arrives too late

**Why it matters:** Visitors may not know whether this is coaching, counselling, career advice, or job-search support. They should be able to self-select before committing attention to a long page or seeing the price.

**Fix:** Put the existing accurate scope line directly under the hero CTA: *For the decisions, patterns, and inner change behind a life or career transition—not job-search, CV, or recruitment support.* Keep the fuller explanation in the at-a-glance block and FAQ.

**Suggested command:** `$impeccable clarify`

### [P1] CTA hierarchy asks new visitors to choose too early

**Why it matters:** “Schedule your discovery call” and “Book your program” imply different readiness levels. Showing both with similar emphasis can create decision friction at the moment reassurance is most needed.

**Fix:** Make the discovery call the single primary conversion action throughout. Present direct booking only after the investment block, with a clear qualifier such as “Already decided?” and secondary visual weight.

**Suggested command:** `$impeccable layout`

### [P2] The visual grammar has become too active

**Why it matters:** The page now uses several card families, image overlays, accordion tiles, and hover-expanding information lists. Each works independently, but together they add interaction noise to what should feel calm and containing.

**Fix:** Reserve expansion for controls that reveal additional content (programme and FAQ). Keep method and outcomes as stable, quietly separated reading rows with an optional subtle hover tint—not a growth animation.

**Suggested command:** `$impeccable quieter`

### [P2] A ready visitor has no fast route to practical details

**Why it matters:** The programme length, format, support, and investment are available, but a visitor ready to compare options must scroll through much of the narrative. Practical clarity is respectful, not overly commercial.

**Fix:** Add small anchor links below the hero CTA—“Programme details”, “Investment”, “Is this right for me?”—or a compact facts strip that points to the existing sections.

**Suggested command:** `$impeccable layout`

## Persona Red Flags

**Maya, the self-reliant overthinker:** She is likely to appreciate the page's insight but may feel she has to keep reading after she already understands the problem. The repeated “stuck/information/patterns” framing risks reinforcing analysis rather than giving her a clean next decision. Give her an early scope and facts route.

**Elena, the cautious first-time coaching visitor:** She needs to know what coaching is and is not before she invests emotionally. The distinction from CV/job-search/recruitment support currently sits away from the hero and after several sections; show it immediately.

**Daniel, ready to act:** He wants duration, format, price, and the next action without reading the full narrative. The existing at-a-glance block is excellent, but an anchor or short route from the hero would make it efficient.

## Minor Observations

- The "Read my story" button's burgundy fill improves hierarchy and works well with the portrait; keep it as the only intentional visual interruption in the proof area.
- The pale-pink bonus tile is calmer than the prior dark version and better fits the offer's supportive tone.
- Consider an early sentence about pace and capacity: the programme can meet a visitor's responsibilities and energy rather than demand a perfect moment for change.
- Keep mobile language controls at least 44 by 44 pixels, even if their visible type remains small.

## Questions to Consider

1. Should this page primarily support a hesitant visitor through the emotional decision, or help a ready visitor self-qualify within the first screen?
2. Does the programme need to feel more like a carefully held therapeutic-style container, or a premium structured service? The copy favors the first; a few tiles and CTAs favor the second.
3. Which message deserves to be the one memorable insight: “Information is not the answer,” “You cannot see your situation objectively,” or “You need a process that changes patterns and actions”? Choosing one would make the page more powerful.
