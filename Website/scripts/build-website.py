#!/usr/bin/env python3
"""Scrape annahellmuth.com and generate static branded HTML in Website/."""

from __future__ import annotations

import hashlib
import html as html_module
import json
import re
import ssl
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parents[1]
MARKETING_ROOT = ROOT.parent
ASSETS = ROOT / "assets" / "images"
DATA_FILE = ROOT / "data" / "pages.json"

SSL_CTX = ssl.create_default_context()

PAGES = [
    ("index", "https://annahellmuth.com/"),
    ("counseling", "https://annahellmuth.com/counseling"),
    ("lifecoaching", "https://annahellmuth.com/lifecoaching"),
    ("about", "https://annahellmuth.com/about"),
    ("contact", "https://annahellmuth.com/contact"),
    ("blog", "https://annahellmuth.com/blog"),
    (
        "blog/blog-post-title-one-3zaa9-zlxng-67tfc-x5jhc",
        "https://annahellmuth.com/blog/Blog%20Post%20Title%20One-3zaa9-zlxng-67tfc-x5jhc",
    ),
    (
        "blog/blog-post-title-two-t5my5-k4xmd-67jzh-cetp9",
        "https://annahellmuth.com/blog/blog-post-title-two-t5my5-k4xmd-67jzh-cetp9",
    ),
    (
        "blog/blog-post-title-three-y3peb-4lwnz-5pkhf-84d88",
        "https://annahellmuth.com/blog/blog-post-title-three-y3peb-4lwnz-5pkhf-84d88",
    ),
    (
        "blog/blog-post-title-four-lr658-tcthp-wf5mw-n7m7y",
        "https://annahellmuth.com/blog/blog-post-title-four-lr658-tcthp-wf5mw-n7m7y",
    ),
    ("impressum", "https://annahellmuth.com/impressum"),
    ("privacy-policy", "https://annahellmuth.com/privacy-policy"),
]

NAV = [
    ("Psychological counseling", "counseling/"),
    ("Life coaching", "lifecoaching/"),
    ("About", "about/"),
    ("Contact", "contact/"),
]

SOCIAL_LINKS = {
    "linkedin": "https://www.linkedin.com/in/anna-hellmuth-408a17201/",
    "facebook": "https://www.facebook.com/drhellmuthanna/",
    "instagram": "https://www.instagram.com/anna_hellmuth.md/",
    "tiktok": "https://www.tiktok.com/@anna_hellmuth.md",
}

TYPEKIT = (
    "https://use.typekit.net/ik/r0p1MYsmR1L75nvVsqVUB5iMYX6V0yf3aSvQ_zx_uSGfe7SIfFHN4UJLFRbh52jhWDjDwRbtwewoFc9DZRj3FQStwQsqwRsRwy79MkG0jAFu-WsoShFGZAsude80ZkoRdhXCHKoyjamTiY8Djhy8ZYmC-Ao1Oco8if37OcBDOcu8OfG0ZcUzihmkOANRZAUzifXkZRJkO1FUiABkZWF3jAF8OcFzdP37O1FUiABkZWF3jAF8ShFGZAsude80ZkoRdhXCjAFu-WsoShFGZAsude80ZkoRdhXCjAFu-WsoShFGZAsude80Zko0ZWbCjAo0jAy8deUliWsGOcFzdPUySkolZPUcdeNaZWJldhF8deNXOQ4cwRJ0SaBujW48Sagyjh90jhNlOeUzjhBC-eNDifUDSWmyScmDSeBRZWFR-emqiAUTdcS0jhNlOYiaikoyjamTiY8Djhy8ZYmC-Ao1OcFzdPUaiaS0jAFu-WsoShFGZAsude80Zko0ZWbCiaiaOcB0dcBGZAUCdWmX-foRdhXCiaiaOcBDOcu8OYiaikocdeNaZWJldhF8deNXOQ4cwRJ0SaBujW48Sagyjh90jhNlOYiaikoDSWmyScmDSeBRZWFR-emqiAUTdcS0jhNlJ6ol-Ao8S1ZyOAuzZemkdKJbZ148-AiGifuXZWyXOWgkdkG4fO9nIMMjgfMfH6qJceqbMs6IJMJ7fbK6-sMgeMj6MKG4f4TTIMIjgkMfH6qJcAqbMs65JMJ7fbKd-sMgegI6MTMg7H2ET6j.js"
)

downloaded_images: dict[str, str] = {}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "MarketingSystemMirror/1.0"})
    with urllib.request.urlopen(req, context=SSL_CTX, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def normalize_url(src: str, base: str) -> str:
    if src.startswith("//"):
        src = "https:" + src
    return urllib.parse.urljoin(base, src)


def local_image(url: str) -> str:
    if url in downloaded_images:
        return downloaded_images[url]
    parsed = urllib.parse.urlparse(url)
    name = Path(parsed.path).name.split("?")[0] or "image"
    if "." not in name:
        name += ".jpg"
    digest = hashlib.md5(url.encode()).hexdigest()[:10]
    safe = re.sub(r"[^a-zA-Z0-9._-]", "-", name)[:80]
    filename = f"{digest}-{safe}"
    dest = ASSETS / filename
    if not dest.exists():
        ASSETS.mkdir(parents=True, exist_ok=True)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "MarketingSystemMirror/1.0"})
            with urllib.request.urlopen(req, context=SSL_CTX, timeout=60) as resp:
                dest.write_bytes(resp.read())
        except urllib.error.URLError as e:
            print(f"  warn: image failed {url}: {e}")
            return url
    downloaded_images[url] = f"assets/images/{filename}"
    return downloaded_images[url]


def prefix_for(slug: str) -> str:
    if slug == "index":
        return ""
    return "../" * len(Path(slug).parts)


def rewrite_links(html: str, page_prefix: str) -> str:
    """Convert absolute annahellmuth paths to local static paths."""
    replacements = [
        (r'href="https://annahellmuth\.com/"', f'href="{page_prefix}"'),
        (r"href='https://annahellmuth\.com/'", f"href='{page_prefix}'"),
        (r'href="https://annahellmuth\.com/([^"]+)"', r'href="' + page_prefix + r"\1\""),
        (r'href="/([^"]*)"', lambda m: f'href="{page_prefix}{m.group(1)}"'),
    ]
    out = html
    out = re.sub(r'href="https://annahellmuth\.com/"', f'href="{page_prefix}"', out)
    out = re.sub(r'href="https://annahellmuth\.com/([^"]*)"', lambda m: f'href="{page_prefix}{m.group(1)}"', out)
    out = re.sub(r'href="/([^"]*)"', lambda m: f'href="{page_prefix}{m.group(1)}"', out)
    return out


def fix_href(href: str, asset_prefix: str) -> str:
    if not href or href.startswith("#") or href.startswith("mailto:"):
        return href
    if href.startswith("/"):
        return asset_prefix + href.lstrip("/")
    if "annahellmuth.com" in href:
        return asset_prefix + href.split("annahellmuth.com/", 1)[-1]
    return href


def sanitize_inline_html(element: Tag, page_url: str, asset_prefix: str) -> str:
    allowed = {
        "p",
        "h1",
        "h2",
        "h3",
        "h4",
        "strong",
        "em",
        "b",
        "i",
        "ul",
        "ol",
        "li",
        "a",
        "br",
        "blockquote",
    }
    clone = BeautifulSoup(str(element), "html.parser")
    root = clone.find(attrs={"data-sqsp-text-block-content": True}) or clone

    for tag in list(root.find_all(True)):
        if tag.name not in allowed:
            tag.unwrap()
            continue
        if tag.name == "a":
            tag["href"] = fix_href(tag.get("href", "#"), asset_prefix)
            tag["class"] = "brand-link"
        for attr in list(tag.attrs):
            if attr not in ("href", "class"):
                del tag[attr]

    return root.decode_contents().strip()


def extract_page(slug: str, url: str) -> dict:
    print(f"Fetching {slug}...")
    html = fetch(url)
    soup = BeautifulSoup(html, "lxml")
    title = (soup.find("title").get_text(strip=True) if soup.find("title") else slug)

    prefix = prefix_for(slug)
    blocks: list[dict] = []

    for section in soup.select("section.page-section, section[data-section-id]"):
        if section.select(".sqs-block-instagram"):
            continue
        classes = " ".join(section.get("class", []))
        theme = "cream"
        if "white" in classes or "bright" in classes:
            theme = "light"
        if "black" in classes or "dark" in classes:
            theme = "burgundy"

        sec_blocks = []
        for img in section.select("img[src]"):
            src = img.get("src") or img.get("data-src")
            if not src or "squarespace" not in src:
                continue
            alt = (img.get("alt") or "").lower()
            if "logo" in src.lower() or (img.get("alt") or "") == "Anna Hellmuth":
                continue
            if alt == "client" or "user-0" in src.lower():
                continue
            if "instagram" in str(section).lower() and section.select(".sqs-block-instagram"):
                continue
            full = normalize_url(src, url)
            local = local_image(full)
            sec_blocks.append(
                {
                    "type": "image",
                    "src": prefix + local,
                    "alt": img.get("alt", ""),
                }
            )

        for tb in section.select("[data-sqsp-text-block-content]"):
            clean = sanitize_inline_html(tb, url, prefix)
            if not clean.strip():
                continue
            sec_blocks.append({"type": "html", "html": clean})

        if sec_blocks and not is_footer_section(sec_blocks):
            blocks.append({"theme": theme, "blocks": sec_blocks})

    blocks = [b for b in blocks if not is_footer_section(b["blocks"])]

    if not blocks:
        for tb in soup.select("[data-sqsp-text-block-content]"):
            clean = sanitize_inline_html(tb, url, prefix)
            if clean.strip():
                blocks.append({"theme": "cream", "blocks": [{"type": "html", "html": clean}]})

    extras = {}
    if slug == "index":
        extras = extract_index_extras(soup, prefix)

    hero_img = None
    for img in soup.select("img[src*='squarespace-cdn']"):
        alt = (img.get("alt") or "").lower()
        src = img.get("src", "")
        if "logo" in src.lower():
            continue
        if any(x in alt for x in ("woman", "holding", "portrait", "anna")) or "image-asset" in src:
            hero_img = prefix + local_image(normalize_url(src, url))
            break

    return {
        "slug": slug,
        "url": url,
        "title": title,
        "blocks": blocks,
        "hero_image": hero_img,
        "extras": extras,
    }


def section_is_stub(section: dict, heading_fragment: str) -> bool:
    html_parts = [b.get("html", "") for b in section.get("blocks", []) if b.get("type") == "html"]
    combined = " ".join(html_parts)
    return heading_fragment in combined and len(html_parts) <= 2


def is_footer_section(blocks: list[dict]) -> bool:
    text = " ".join(b.get("html", "") for b in blocks if b.get("type") == "html")
    return "Copyright" in text and "Impressum" in text


def extract_index_extras(soup: BeautifulSoup, prefix: str) -> dict:
    testimonials = []
    for card in soup.select(".testimonial-card"):
        paras = [p.get_text(" ", strip=True) for p in card.select("p")]
        quote = " ".join(paras).strip()
        if quote:
            testimonials.append(quote)

    faq_items = []
    for item in soup.select(".accordion-item"):
        q_el = item.select_one(".accordion-item__title")
        a_el = item.select_one(".accordion-item__description")
        if q_el and a_el:
            faq_items.append((q_el.get_text(strip=True), a_el.get_text("\n", strip=True)))

    return {"testimonials": testimonials, "faq": faq_items}


def render_services_grid(prefix: str) -> str:
    return f"""
    <section class="section section--light">
      <div class="container">
        <div class="services-grid">
          <article class="card-service">
            <h3 class="card-service__title">Psychological counseling</h3>
            <p class="card-service__body">Find your power to release emotional burdens and heal your soul</p>
            <a class="btn-secondary" href="{prefix}counseling/">Discover Counseling Services</a>
          </article>
          <article class="card-service">
            <h3 class="card-service__title">Life coaching</h3>
            <p class="card-service__body">Realize your ambitious goals and ascend to new heights</p>
            <a class="btn-secondary" href="{prefix}lifecoaching/">Explore Coaching Details</a>
          </article>
        </div>
      </div>
    </section>"""


def render_testimonials(testimonials: list[str]) -> str:
    cards = []
    for quote in testimonials:
        safe = html_module.escape(quote)
        cards.append(
            f'<blockquote class="quote-testimonial"><p class="quote-testimonial__text">“{safe}”</p>'
            f'<cite class="quote-testimonial__cite">— Former client*</cite></blockquote>'
        )
    return (
        f'<section class="section section--burgundy"><div class="container">'
        f'<h2 class="text-h2 text-on-dark">What my clients are saying about working with me</h2>'
        f'<p class="text-on-dark text-caption"><em>* feedback from clients is posted anonymously to protect their privacy</em></p>'
        f'<div class="testimonials">{"".join(cards)}</div></div></section>'
    )


def render_faq(faq: list[tuple[str, str]]) -> str:
    items = []
    for q, a in faq:
        items.append(
            f'<details class="faq-details"><summary>{html_module.escape(q)}</summary>'
            f"<p>{html_module.escape(a)}</p></details>"
        )
    return (
        f'<section class="section section--cream"><div class="container">'
        f'<h2 class="text-h2">Frequently asked questions</h2>'
        f'<div class="faq-list">{"".join(items)}</div></div></section>'
    )


def render_nav(prefix: str, active: str) -> str:
    home = prefix or "./"
    items = [f'<a href="{home}">Home</a>']
    for label, href in NAV:
        path = (prefix + href).rstrip("/")
        cls = ' class="is-active"' if active.rstrip("/") == href.rstrip("/") else ""
        items.append(f'<a href="{prefix}{href}"{cls}>{label}</a>')
    items.append(f'<a href="{prefix}blog/">Blog</a>')
    return "\n          ".join(items)


BLOG_POSTS = [
    ("blog/blog-post-title-one-3zaa9-zlxng-67tfc-x5jhc/", "Blog Post Title One"),
    ("blog/blog-post-title-two-t5my5-k4xmd-67jzh-cetp9/", "Blog Post Title Two"),
    ("blog/blog-post-title-three-y3peb-4lwnz-5pkhf-84d88/", "Blog Post Title Three"),
    ("blog/blog-post-title-four-lr658-tcthp-wf5mw-n7m7y/", "Blog Post Title Four"),
]


def render_blog_index(prefix: str) -> str:
    items = "\n".join(
        f'<li><a href="{prefix}{href}">{title}</a></li>' for href, title in BLOG_POSTS
    )
    return f"""
    <section class="section section--cream">
      <div class="container">
        <h1 class="text-h2">Blog</h1>
        <p class="text-body">Insights on counseling, coaching, and personal growth.</p>
        <ul class="blog-list">{items}</ul>
      </div>
    </section>"""


def render_page(page: dict) -> str:
    slug = page["slug"]
    prefix = prefix_for(slug)
    css_href = prefix + "css/site.css"
    js_href = prefix + "js/site.js"
    logo_src = prefix + "assets/images/logo.png"
    active = "" if slug == "index" else slug + "/"

    sections_html = []
    for i, section in enumerate(page["blocks"]):
        theme_class = {
            "cream": "section--cream",
            "light": "section--light",
            "burgundy": "section--burgundy",
        }.get(section["theme"], "section--cream")
        inner = []
        for block in section["blocks"]:
            if block["type"] == "image":
                inner.append(
                    f'<figure class="content-figure"><img src="{block["src"]}" alt="{block["alt"]}" loading="lazy" /></figure>'
                )
            else:
                inner.append(f'<div class="content-rich">{block["html"]}</div>')
        sections_html.append(
            f'<section class="section {theme_class}"><div class="container">{"".join(inner)}</div></section>'
        )

    if slug == "index" and page.get("hero_image") and page["blocks"]:
        first = page["blocks"][0]
        first["blocks"] = [b for b in first["blocks"] if b.get("type") != "image"]
        if first["blocks"] and first["blocks"][0]["type"] == "html":
            first["blocks"] = first["blocks"][2:]
        if not first["blocks"]:
            page["blocks"].pop(0)
        page["blocks"] = [b for b in page["blocks"] if not is_footer_section(b["blocks"])]
        page["blocks"] = [
            b
            for b in page["blocks"]
            if not section_is_stub(b, "What my clients are saying")
            and not section_is_stub(b, "Frequently asked questions")
        ]

    hero = ""
    if slug == "index" and page.get("hero_image"):
        hero = f"""
    <section class="hero section--burgundy">
      <div class="container hero__grid">
        <div class="hero__copy">
          <h1 class="text-h2 text-on-dark">Online counseling and coaching for creative &amp; ambitious souls</h1>
          <p class="text-on-dark text-body">Available wherever you are, in English, German, Ukrainian, Russian, or a mix of them all</p>
          <p><a class="btn-primary" href="{prefix}contact/">Schedule your discovery call</a></p>
        </div>
        <div class="hero__media">
          <img src="{page["hero_image"]}" alt="Anna Hellmuth" />
        </div>
      </div>
    </section>"""

    body = hero + "\n".join(sections_html)
    if slug == "index":
        extras = page.get("extras") or {}
        injected = []
        for i, section in enumerate(sections_html):
            injected.append(section)
            if "My services" in section and "services-grid" not in section:
                injected.append(render_services_grid(prefix))
        if extras.get("testimonials"):
            injected.append(render_testimonials(extras["testimonials"]))
        if extras.get("faq"):
            injected.append(render_faq(extras["faq"]))
        body = hero + "\n".join(injected if injected else sections_html)
    if slug == "blog":
        body = render_blog_index(prefix) + body

    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{page["title"]}</title>
    <meta name="description" content="Anna Hellmuth — Psychological Counseling &amp; Life Coaching" />
    <link rel="preconnect" href="https://use.typekit.net" crossorigin />
    <script src="{TYPEKIT}" async></script>
    <script>try{{Typekit.load();}}catch(e){{}}</script>
    <link rel="stylesheet" href="{css_href}" />
  </head>
  <body>
    <header class="site-header">
      <div class="container site-header__inner">
        <a class="site-logo" href="{prefix or './'}">
          <img src="{logo_src}" alt="Anna Hellmuth" width="160" />
        </a>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
        <nav id="site-nav" class="site-nav" aria-label="Main">
          {render_nav(prefix, active)}
          <a class="btn-primary btn-primary--nav" href="{prefix}contact/">Schedule your discovery call</a>
        </nav>
      </div>
    </header>
    <main>
{body}
    </main>
    <footer class="site-footer section--burgundy">
      <div class="container site-footer__grid">
        <div>
          <p class="text-on-dark text-body">Anna Hellmuth Psychological Counseling and Life Coaching</p>
          <p class="text-on-dark"><a class="brand-link text-on-dark" href="mailto:contact@annahellmuth.com">contact@annahellmuth.com</a></p>
        </div>
        <div>
          <p class="text-on-dark text-small">Follow me</p>
          <p class="text-on-dark text-small">
            <a class="brand-link text-on-dark" href="{SOCIAL_LINKS["linkedin"]}" rel="noopener noreferrer">LinkedIn</a> ·
            <a class="brand-link text-on-dark" href="{SOCIAL_LINKS["facebook"]}" rel="noopener noreferrer">Facebook</a> ·
            <a class="brand-link text-on-dark" href="{SOCIAL_LINKS["instagram"]}" rel="noopener noreferrer">Instagram</a> ·
            <a class="brand-link text-on-dark" href="{SOCIAL_LINKS["tiktok"]}" rel="noopener noreferrer">TikTok</a>
          </p>
        </div>
        <div>
          <p class="text-on-dark text-small">
            <a class="brand-link text-on-dark" href="{prefix}impressum/">Impressum – Legal Notice</a><br />
            <a class="brand-link text-on-dark" href="{prefix}privacy-policy/">Privacy Policy</a>
          </p>
          <p class="text-on-dark text-caption">Copyright © 2025 Anna Hellmuth</p>
        </div>
      </div>
    </footer>
    <script src="{js_href}"></script>
  </body>
</html>
"""


def main():
    import shutil

    logo_src = MARKETING_ROOT / "brand" / "assets" / "logo" / "logo.png"
    ASSETS.mkdir(parents=True, exist_ok=True)
    shutil.copy(logo_src, ASSETS / "logo.png")

    pages_data = []
    for slug, url in PAGES:
        try:
            page = extract_page(slug, url)
            pages_data.append(page)
        except Exception as e:
            print(f"ERROR {slug}: {e}")

    global BLOG_POSTS
    BLOG_POSTS = []
    for p in pages_data:
        if p["slug"].startswith("blog/"):
            title = p["title"].split("—")[0].strip() if "—" in p["title"] else p["title"]
            BLOG_POSTS.append((p["slug"] + "/", title))

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(pages_data, indent=2), encoding="utf-8")

    for page in pages_data:
        slug = page["slug"]
        out_dir = ROOT / slug if slug != "index" else ROOT
        if slug != "index":
            out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "index.html"
        html = render_page(page)
        out_file.write_text(html, encoding="utf-8")
        print(f"Wrote {out_file}")

    print(f"Done. {len(downloaded_images)} images, {len(pages_data)} pages.")


if __name__ == "__main__":
    main()
