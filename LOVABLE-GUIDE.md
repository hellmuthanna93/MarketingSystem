# Lovable build guide - Anna Hellmuth

**Purpose:** Single reference for rebuilding or extending [annahellmuth.com](https://annahellmuth.com) in [Lovable](https://lovable.dev) (or any React/Next app). This repo is the source of truth for brand, copy, structure, and marketing strategy.

**Practice:** Online psychological counseling & life coaching  
**Owner:** Anna Hellmuth - medical doctor, psychologist, life coach  
**Primary audience label:** *creative & ambitious souls*  
**Languages:** English, German, Ukrainian, Russian (sessions and marketing)

---

## Table of contents

1. [What to build](#1-what-to-build)
2. [Brand identity](#2-brand-identity)
3. [Typography](#3-typography)
4. [Layout & spacing](#4-layout--spacing)
5. [Components](#5-components)
6. [Site map & pages](#6-site-map--pages)
7. [Homepage section spec](#7-homepage-section-spec)
8. [Approved copy & CTAs](#8-approved-copy--ctas)
9. [Voice & content strategy](#9-voice--content-strategy)
10. [Positioning & audience](#10-positioning--audience)
11. [Services & pricing](#11-services--pricing)
12. [Blog (SEO)](#12-blog-seo)
13. [FAQ content](#13-faq-content)
14. [Testimonials](#14-testimonials)
15. [Contact & social](#15-contact--social)
16. [Legal & footer](#16-legal--footer)
17. [SEO & meta](#17-seo--meta)
18. [Assets & imagery](#18-assets--imagery)
19. [Do / don't](#19-do--dont)
20. [Repo reference](#20-repo-reference)

---

## 1. What to build

A calm, feminine, premium wellness practice site for **international professionals and creatives** seeking either:

- **Psychological counseling** - healing, emotional processing, mental wellbeing  
- **Life coaching** - goals, structure, ambitious life redesign  

**Core conversion:** Free **30-minute discovery call** → paid counseling or coaching.

**Design feel:** Burgundy + warm cream (not stark white). Serif typography. Generous whitespace. Soft cards with subtle borders. No hustle/grind aesthetic. Movement-first copy (transformation, relief, clarity - not “book a session” as the hook).

**Tech note for Lovable:** Port CSS variables below into `globals.css` or Tailwind theme extension. Load **Source Serif 4** from Google Fonts. No Adobe Typekit.

---

## 2. Brand identity

### Colors (use exactly - define once in theme)

| Token | Hex / value | Usage |
|-------|-------------|--------|
| Accent (burgundy) | `#64010d` | Primary buttons, FAQ section bg, footer |
| Accent hover | `#4a0202` | Button hover |
| Text | `#5c020c` | Headings & body on light backgrounds |
| Text on dark | `#ffffff` | Text on burgundy |
| Surface light | `#fefbf6` | Hero, services, steps, blog, intake - **primary page bg** |
| Surface cream | `#f7eae3` | Testimonials, opportunity checklist - **secondary sections** |
| White | `#ffffff` | Cards on cream sections |
| Border | `rgba(92, 2, 12, 0.15)` | Dividers |
| Border card | `rgba(100, 1, 13, 0.14)` | Service & testimonial cards |

### Section background rhythm (homepage)

| Section | Background |
|---------|------------|
| Header | `#fefbf6` (light cream) |
| Hero | `#fefbf6` |
| Services | `#fefbf6` |
| Testimonials | `#f7eae3` |
| Steps (journey) | `#fefbf6` |
| Opportunity checklist | `#f7eae3` |
| FAQ | `#64010d` (burgundy) with **one cream accordion panel** inside |
| Get to know me + calendar + Instagram | `#fefbf6` |
| Footer | `#64010d` |

### CSS variables (copy-paste ready)

```css
:root {
  --color-accent: #64010d;
  --color-accent-hover: #4a0202;
  --color-text: #5c020c;
  --color-text-on-dark: #ffffff;
  --color-surface: #f7eae3;
  --color-surface-light: #fefbf6;
  --color-border: rgba(92, 2, 12, 0.15);
  --color-border-card: rgba(100, 1, 13, 0.14);
  --color-bg-primary: var(--color-surface-light);
  --color-bg-secondary: var(--color-surface);
  --color-bg-dark: var(--color-accent);
  --radius-pill: 300px;
  --radius-card: 20px;
  --layout-max-width: 75rem;
  --layout-content-width: 42rem;
}
```

---

## 3. Typography

**Font:** [Source Serif 4](https://fonts.google.com/specimen/Source+Serif+4) - single family for headings and body.

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
```

Google Fonts import:

```css
@import url("https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,200..900;1,8..60,200..900&display=swap");

--font-family: "Source Serif 4", Georgia, "Times New Roman", serif;
```

### Weights

| Role | Weight | Notes |
|------|--------|--------|
| Headings (h1-h4) | **600** semibold | Not 700 bold |
| Body prose | **400** regular | |
| Nav links | **400** | |
| Buttons | **400** regular | Intentionally not bold |
| Labels, kickers, badges, emphasis | **600** | |
| Pricing figures | **500** medium | |

### Scale (desktop reference)

- H1 hero: `clamp(1.8rem, 4.5vw, 3rem)`
- H2 section: `clamp(1.6rem, 4vw, 2.5rem)`
- Body: `1rem`-`1.05rem`, line-height `1.7`-`1.8`
- Large intro: `1.15rem`-`1.2rem`
- Button (in-page): `1.2rem`
- Button (nav): `0.9rem`, padding `0.625rem 1.35rem`

**Heading color on cream sections:** `#5c020c` (text color) - **not** burgundy. Burgundy is for buttons and accents only on light bg.

---

## 4. Layout & spacing

- **Max content width:** `75rem` (1200px)
- **Prose / article width:** `42rem`
- **Section padding:** `clamp(4rem, 8vw, 8rem)` vertical
- **Container:** 90% width, centered
- **Header height:** ~180px default (stacked logo + nav); shrinks to ~80px on scroll (optional enhancement in static mirror)

---

## 5. Components

### Header

- Logo centered above nav on desktop (stacked layout)
- Nav links: **Psychological counseling** · **Life coaching** · **About** · **Blog** · **Contact**
- Nav sentence case on live-aligned mirror (`counseling` not `Counseling` in link labels - either is acceptable; mirror uses sentence case)
- Right CTA: **Schedule your discovery call** - compact pill button
- Background: light cream `#fefbf6`

### Primary button `.btn-primary`

- Background `#64010d`, text white
- Border-radius `300px` (full pill)
- Padding in-page: ~`1.1rem 2rem`
- Font weight **400**
- Hover: `#4a0202`

### Service cards

- White background
- Border `2px solid rgba(100, 1, 13, 0.14)`
- Border-radius **20px**
- Padding ~`2.5rem` horizontal up to `5rem` on wide screens
- Centered text
- Full-width pill CTA inside card

### Testimonial cards

- White on cream section `#f7eae3`
- Border `2px solid rgba(100, 1, 13, 0.14)`, radius `12px`
- Padding `1.5rem 2rem`
- Attribution: **- Former client*** with round avatar
- Privacy note above grid: *feedback from clients is posted anonymously to protect their privacy*

### FAQ (burgundy section)

- Section bg `#64010d`, h2 white
- **Single cream panel** `#fefbf6`, radius `20px`, generous padding
- Accordion items inside panel with dividers - **not** separate floating white cards
- Question text burgundy `#64010d`, body `#5c020c`

### Opportunity checklist

- Section bg cream `#f7eae3`
- White card with **2px burgundy border**, radius `12px`
- Checkmarks + prose in text color (not burgundy body)

### Steps section

- Three text blocks in a row: **Step 1:** … **Step 2:** … **Step 3:** …
- No burgundy circles (legacy design removed)
- Step 3 copy includes **transformation journey**

### Blog cards

- White card, 20px radius, 2px border-card
- Tag uppercase, title semibold, excerpt, read time

---

## 6. Site map & pages

| Route | Page | Purpose |
|-------|------|---------|
| `/` | Home | Main conversion funnel |
| `/counseling` | Psychological counseling | Service detail + pricing |
| `/lifecoaching` | Life coaching | Service detail + pricing |
| `/about` | About | Trust, credentials, story, FAQ |
| `/contact` | Contact | Email, office, calendar embed |
| `/blog` | Blog index | SEO content hub |
| `/blog/[slug]` | Blog post | Long-form articles |
| `/impressum` | Legal notice | DE legal requirement |
| `/privacy-policy` | Privacy policy | GDPR |

**Primary CTA everywhere:** [Discovery call calendar](https://calendar.app.google/ueKb9RbyxWyC6zfK8)

---

## 7. Homepage section spec

Build in this order:

1. **Hero** - H1 + italic subhero + portrait image + transformation copy + CTA  
2. **Invitation block** - “Don't wait for someday…” + “Why not give it a try and find out!”  
3. **My services** - 2 cards (counseling + coaching)  
4. **Testimonials** - grid of white cards (desktop: mixed 2-col layouts; mobile: shortened quotes)  
5. **Journey steps** - 3 text steps + CTA  
6. **Opportunity** - “A free 30-minute session with me is an opportunity for you to…” + 4 check items  
7. **FAQ** - 7 questions, burgundy bg, cream accordion  
8. **Get to know me** - H2, Google Calendar embed, Instagram 4×2 grid (no separate “Follow me” H2 - combined section like live site)  
9. **Footer** - logo, nav, contact, social icons, legal links  

---

## 8. Approved copy & CTAs

### Headlines & taglines

| Context | Copy |
|---------|------|
| Hero H1 | Online psychological counseling and life coaching |
| Subhero | Available wherever you are, in English, German, Ukrainian, Russian, or a mix of them all |
| Transformation | Shape your future self. / Take the first step today. |
| Invitation | Don't wait for "someday," struggling against the tide alone. |
| Soft close | Why not give it a try and find out! |
| Services intro | From navigating life's difficulties to striving for greater fulfillment, I provide options designed to support your unique path |
| Footer tagline | Empowering creative & ambitious souls to achieve mental well-being and personal alignment. |

### Service cards (home)

| Service | Title | Description | CTA |
|---------|-------|-------------|-----|
| Counseling | Psychological counseling | Find your power to release emotional burdens and heal your soul | Discover Counseling Services |
| Coaching | Life coaching | Realize your ambitious goals and ascend to new heights | Explore Coaching Details |

### Service page H1s

| Page | H1 |
|------|-----|
| Counseling | You don't have to face this alone |
| Coaching | You need a courageous heart to claim the life you want |
| About | About me |
| Contact | Contact |
| Blog | Insights for creative & ambitious souls |

### About lead

> My name is Anna Hellmuth. I'm a medical doctor, psychologist, and life coach.  
> I empower individuals to achieve greater well-being through transformative journeys, integrating medical and psychological expertise.

### CTAs (priority order)

1. **Schedule your discovery call** (primary - nav, hero, sections)  
2. **Discover Counseling Services**  
3. **Explore Coaching Details**  
4. **Learn more about me**  
5. **contact@annahellmuth.com**

### Emotional hooks (reuse in content)

- *The thought of a life unlived is a potent call to action*
- *We are our own toughest critics, our own most persistent roadblocks*
- *With the right guidance and dedicated support, those challenges become stepping stones*
- *Working with a fitting professional will make your progress remarkably faster and lighter, saving you years of precious time*

---

## 9. Voice & content strategy

### Tone

- Warm, professional, empowering - never clinical or cold  
- Validates difficulty; emphasizes support and faster progress with the right fit  
- Honest about limits (no guaranteed outcomes)  
- Use **you**; full sentences on web  

### Core marketing principle

**People buy movement, not coaching.**

Communicate: relief, hope, clarity, confidence, possibility, transformation - **not** the method, session format, or credential list in hooks.

### Strong content formula

```
You think X.
Actually, Y is happening.
That is why Z feels so difficult.
```

### Content checklist (before publishing)

- Does this describe a real human experience?
- Would someone recognize themselves?
- Does it make the reader feel **seen**?
- Does it demonstrate how Anna thinks (subtle business value)?
- Movement-first opening?

### Prefer / avoid

| Prefer | Avoid |
|--------|--------|
| transformation, clarity, relief, patterns, roadblocks | guaranteed results, miracle, fix you |
| courageous, authentic, resonate | hustle, grind, 10x |
| discovery call, mutual fit | limited spots, act now, guilt pressure |
| - Former client* (anonymous) | Identifying client details |

### Weekly content mix

- **1 counseling post/week** - shame, boundaries, attachment, regulation, childhood patterns  
- **1 coaching post/week** - fear & action, purpose, transitions, authentic success  

---

## 10. Positioning & audience

### Who it's for

Highly educated professionals, creatives, entrepreneurs - functioning externally, stuck internally.

**Public label:** creative & ambitious souls

### Counseling vs coaching

| | Counseling | Coaching |
|---|------------|----------|
| Focus | Healing, emotions, past | Goals, structure, future |
| Tagline | Release emotional burdens and heal your soul | Realize ambitious goals and ascend to new heights |
| Ask | Emotional/past-focused? | Goal/future-focused? |

### Ideal client qualities (about page)

- Understand growth requires effort  
- Embrace depth over quick fixes  
- Open-minded & curious  
- Refuse to settle  
- Follow intuition when something feels right  

### Credentials (trust pages only - not social hooks)

- MD - Bogomolets National Medical University (Ukraine); University of Würzburg (Germany)  
- Psychologist & coach - Institute of Effective Psychology and Psychotherapy of Zina Shamoyan (Russia)  
- Hypnotherapist (ongoing) - Milton Erickson Society for Clinical Hypnosis (Germany)  
- Online practice since 2023  
- Integrative: humanistic + hypnotherapy, psychodynamic, CBT, systemic constellations  

### Business context (internal - tone reference)

- 2026 focus: consistent content, audience trust, coaching growth, calm lifestyle  
- Long-term: profitable practice, quality clients, max ~6-7 hours/day, 2 free days/week  

---

## 11. Services & pricing

Payment on booking. Free cancel/reschedule **48+ hours** before; full fee within 48 hours.

### Psychological counseling

| Option | Price |
|--------|-------|
| Single session (60 min) | €120 |
| 6-session package (recommended) | €660 (€110/session) |

### Life coaching

The 16-week 1:1 coaching program is the only coaching offer. It includes 12
core sessions, weekly written support, live hypno-meditations during relevant
sessions, a personal transition plan, and a follow-up one month later.

**Price:** TBD

Coaching single sessions, Basic Breakthrough, and Profound Transformation are
retired.

### Discovery call

- **Free 30 minutes**  
- Mutual fit - not therapy  
- Clarify counseling vs coaching  
- [Book here](https://calendar.app.google/ueKb9RbyxWyC6zfK8)

---

## 12. Blog (SEO)

**Index:** `/blog` - “Insights for creative & ambitious souls”

### Published posts (build these routes)

| Slug | Title | SEO focus |
|------|-------|-----------|
| `counseling-vs-life-coaching` | Counseling vs life coaching: how to know what you need | counseling vs coaching, which do I need |
| `online-counseling-for-expats` | Online counseling when you live between countries - and languages | online therapy expats, multilingual counseling |
| `burnout-when-success-feels-empty` | When success on the outside does not match how you feel inside | burnout high achievers, ambitious professionals |
| `signs-you-need-professional-support` | Signs you are carrying more than you should have to alone | when to seek therapy, need a therapist |

Each post: meta title + description, breadcrumb, movement-first dek, 600-900 words, internal links to services, discovery CTA, related posts.

---

## 13. FAQ content

Use on homepage (and optionally about). Seven items:

1. **Can I not address my inner issues on my own? Do I really need someone else's help?**  
   There are times when self-reliance is sufficient, and times when it's not. A skilled specialist can save you years…

2. **What's the difference between psychological counseling and life coaching?**  
   Counseling = emotional/past-focused healing. Coaching = goals/future-focused structure. Ask: emotional vs directional pain?

3. **What methods are you using in your work?**  
   Integrative, humanistic foundation; hypnotherapy, psychodynamic, CBT, systemic constellations as needed.

4. **Can you guarantee the results I'm looking for?**  
   No specific guarantees; resources and support provided; best results from engaged clients who integrate insights.

5. **I work 9 to 5. Can I book evening or weekend appointments?**  
   Prefer well-rested sessions; some evening/weekend slots for time zones and schedules.

6. **What happens if I have to cancel an appointment?**  
   Free reschedule/cancel 48+ hours before; full fee inside 48 hours.

7. **Can we work together if I'm still figuring out what I want?**  
   Yes - clarity itself can be the goal.

---

## 14. Testimonials

- Long-form quotes on desktop; shortened versions on mobile  
- Always **- Former client***  
- Privacy: *feedback from clients is posted anonymously to protect their privacy*  
- Themes to echo in marketing: pattern awareness, relief from first session, tailored rational explanations, deep childhood work, warmth/safety, life overhaul (divorce, career, finances, relationship)

Do not invent new testimonial text without client approval.

---

## 15. Contact & social

| Channel | Value |
|---------|--------|
| Email | contact@annahellmuth.com |
| Office | Erhardstraße 13, 90482 Nuremberg, Germany |
| Discovery call | https://calendar.app.google/ueKb9RbyxWyC6zfK8 |
| Instagram | https://www.instagram.com/anna_hellmuth.md/ (@anna_hellmuth.md) |
| LinkedIn | https://www.linkedin.com/in/anna-hellmuth-408a17201/ |
| Facebook | https://www.facebook.com/drhellmuthanna/ |
| TikTok | https://www.tiktok.com/@anna_hellmuth.md |
| Directory badge | locationindependenttherapists.com/therapists/anna-hellmuth/ |

---

## 16. Legal & footer

- © 2025 Anna Hellmuth. All rights reserved.  
- **Legal Notice (Impressum)** - required for DE  
- **Privacy Policy** - GDPR  
- Practice name: Anna Hellmuth Psychological Counseling and Life Coaching  

---

## 17. SEO & meta

### Homepage meta example

- **Title:** Anna Hellmuth | Psychological Counseling & Life Coaching  
- **Description:** Online psychological counseling and life coaching. Expert mental health support and personal development in English, German, Ukrainian, and Russian.  

### Practices

- One H1 per page  
- Semantic headings (H2 for sections)  
- Meta description 150-160 chars per page  
- Alt text on images (portrait, Instagram previews)  
- Internal links between blog ↔ services ↔ discovery call  
- `theme-color`: `#64010d`  

### Target keywords (non-exhaustive)

- online psychological counseling  
- life coaching for creatives  
- therapy in English German Ukrainian Russian  
- counseling vs life coaching  
- online therapist expat  
- burnout ambitious professionals  
- Anna Hellmuth psychologist  

---

## 18. Assets & imagery

**In repo:** `website/anna-hellmuth/assets/images/`

- `logo.png` - header/footer  
- `favicon.ico`  
- Hero portrait: `1bc23666-cb2a-40a2-8735-5029651e0064.jpg`  
- Testimonial avatars: `user_01a.png`, `03.png`, etc.  
- Instagram grid: `image-asset.jpeg` … `image-asset_7.jpeg`  
- Badge: `location-independent-therapists.png`  

**Style:** Warm, professional portraits; no stock “shouting therapist” clichés. Hero image ~aspect ratio 1.15, radius 12px, no heavy shadow on live-aligned design.

---

## 19. Do / don't

### Do

- Use burgundy + two-tone cream backgrounds  
- Source Serif 4, heading weight 600, button weight 400  
- Lead with emotional recognition in marketing copy  
- Keep discovery call as primary CTA  
- Support EN / DE / UK / RU messaging  
- Be honest about no guaranteed outcomes  

### Don't

- Hardcode hex outside theme/tokens  
- Use orange palette from legacy `projects/table/` (Phase 2 exception)  
- Use hustle/bro-marketing tone  
- Put credential lists in social hooks  
- Use guilt/urgency CTAs  
- Separate white FAQ cards on burgundy (use single cream accordion block)  
- Use burgundy for body headings on cream (use `#5c020c`)  

---

## 20. Repo reference

This Markdown summarizes the **MarketingSystem** repo. For implementation detail:

| Need | Path |
|------|------|
| Design tokens | `brand/tokens.css` |
| Typography | `brand/typography.css` |
| Components | `brand/components.css` |
| Site layout/CSS | `website/anna-hellmuth/assets/css/index.css` |
| Blog CSS | `website/anna-hellmuth/assets/css/blog.css` |
| Static HTML mirror | `website/anna-hellmuth/` |
| Blog posts | `website/anna-hellmuth/blog/` |
| Voice | `brand/voice.md` |
| Marketing strategy | `brand/marketing/*.md` |
| Visual preview | `styleguide/index.html` |
| Component library | `design-system/index.html` |
| Social templates 1080×1080 | `projects/social/templates/` |

**Local preview:**

```bash
python3 -m http.server 8080
# → http://localhost:8080/website/anna-hellmuth/
# → http://localhost:8080/website/anna-hellmuth/blog/
```

---

## Lovable prompt starter (paste into project)

> Build a responsive marketing website for Anna Hellmuth, an online psychological counselor and life coach for "creative & ambitious souls." Use burgundy `#64010d` and cream backgrounds `#fefbf6` / `#f7eae3`. Font: Source Serif 4 from Google Fonts - headings 600, body and buttons 400. Primary CTA: "Schedule your discovery call" linking to Google Calendar. Pages: Home, Counseling, Life Coaching, About, Blog (4 SEO posts), Contact, Legal, Privacy. Homepage: hero, services, testimonials, steps, opportunity checklist, FAQ on burgundy with cream accordion, calendar + Instagram grid. Tone: warm, movement-first, no hustle. Multilingual sessions: EN, DE, UK, RU. Pricing: counseling €120/session, coaching €180/session. Follow the full spec in LOVABLE-GUIDE.md.

---

*Last synced with MarketingSystem repo - Anna Hellmuth brand, Source Serif 4, blog, and live-site-aligned section colors.*
