#!/usr/bin/env python3
"""
Build HTML documentation site from business-site/docs/**/*.md

Usage:
  python3 business-site/build-html.py
  python3 -m http.server 4173   # → http://localhost:4173/business-site/site/

Source of truth: docs/  ·  Generated output: site/  (do not hand-edit site/)
"""

from __future__ import annotations

import html
import os
import re
import shutil
from pathlib import Path, PurePosixPath

import markdown
from markdown.extensions import fenced_code, tables, nl2br

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
ASSETS_SRC = ROOT / "assets"
README = ROOT / "README.md"

SECTIONS = [
    ("start", "Start", [
        ("00-overview.md", "Practice overview"),
        ("../README.md", "How this suite works"),
    ]),
    ("01-strategy", "01 · Strategy", [
        ("01-strategy/01-vision-mission-values.md", "Vision, mission & values"),
        ("01-strategy/02-positioning-and-niche.md", "Positioning & niche"),
        ("01-strategy/03-ideal-client-profile.md", "Ideal client profile"),
        ("01-strategy/04-market-and-competitors.md", "Market & competitors"),
        ("01-strategy/05-swot.md", "SWOT analysis"),
        ("01-strategy/06-business-model.md", "Business model"),
        ("01-strategy/07-pricing-and-packaging.md", "Pricing & packaging"),
        ("01-strategy/08-business-plan.md", "Business plan"),
    ]),
    ("02-brand", "02 · Brand", [
        ("02-brand/01-brand-strategy.md", "Brand strategy"),
        ("02-brand/02-naming.md", "Naming"),
        ("02-brand/03-visual-identity.md", "Visual identity"),
        ("02-brand/04-voice-and-tone.md", "Voice & tone"),
        ("02-brand/05-messaging.md", "Messaging"),
        ("02-brand/06-logo-concepts.md", "Logo & mark"),
        ("02-brand/07-voice-reference.md", "Voice reference"),
        ("02-brand/08-design-system.md", "Design system"),
    ]),
    ("03-offerings", "03 · Offerings", [
        ("03-offerings/01-service-catalog.md", "Service catalog"),
        ("03-offerings/02-wedge-offer-clarity-session.md", "Clarity Session (wedge)"),
        ("03-offerings/03-retainers-and-packages.md", "Packages"),
        ("03-offerings/04-products-and-tooling.md", "Products & tooling"),
        ("03-offerings/05-case-study-strategy.md", "Case study strategy"),
    ]),
    ("04-marketing", "04 · Marketing", [
        ("04-marketing/01-marketing-strategy.md", "Marketing strategy"),
        ("04-marketing/02-content-engine.md", "Content engine"),
        ("04-marketing/03-channels.md", "Channels"),
        ("04-marketing/04-lead-generation.md", "Lead generation"),
        ("04-marketing/05-website-plan.md", "Website plan"),
        ("04-marketing/06-outreach-compliance-germany.md", "Outreach compliance"),
        ("04-marketing/07-outreach-plan.md", "Outreach plan"),
        ("04-marketing/08-marketing-funnel.md", "Marketing funnel"),
        ("04-marketing/09-international-considerations.md", "International"),
    ]),
    ("05-sales", "05 · Sales", [
        ("05-sales/01-sales-process.md", "Sales process"),
        ("05-sales/02-discovery-to-wedge-script.md", "Discovery → wedge"),
        ("05-sales/03-counseling-agreement.md", "Counseling agreement"),
        ("05-sales/04-onboarding.md", "Onboarding"),
    ]),
    ("06-operations", "06 · Operations", [
        ("06-operations/01-tools-and-stack.md", "Tools & stack"),
        ("06-operations/02-delivery-workflow.md", "Delivery workflow"),
        ("06-operations/03-sops.md", "SOPs index"),
        ("06-operations/04-quality-bar.md", "Quality bar"),
    ]),
    ("07-finance-legal", "07 · Finance & Legal", [
        ("07-finance-legal/01-legal-setup-germany.md", "Legal setup (Germany)"),
        ("07-finance-legal/02-finance-model.md", "Finance model"),
        ("07-finance-legal/03-savings-and-cushion.md", "Savings & runway"),
        ("07-finance-legal/04-templates.md", "Documents checklist"),
        ("07-finance-legal/05-financial-projections.md", "Projections"),
    ]),
    ("08-roadmap", "08 · Roadmap", [
        ("08-roadmap/01-90-day-launch.md", "90-day launch"),
        ("08-roadmap/02-transition-to-fulltime.md", "Growth milestones"),
        ("08-roadmap/03-milestones-and-kpis.md", "Milestones & KPIs"),
        ("08-roadmap/04-task-backlog.md", "Master backlog"),
    ]),
    ("09-toolkit", "09 · Toolkit", [
        ("09-toolkit/00-toolkit-index.md", "Toolkit index"),
        ("09-toolkit/01-discovery-call-script.md", "Discovery call script"),
        ("09-toolkit/02-instagram-launch-posts.md", "IG launch posts"),
        ("09-toolkit/03-linkedin-launch-posts.md", "LinkedIn launch posts"),
        ("09-toolkit/04-content-calendar-90day.md", "90-day calendar"),
        ("09-toolkit/05-client-emails.md", "Client emails"),
        ("09-toolkit/06-wedge-deliverable-template.md", "Wedge deliverable"),
        ("09-toolkit/07-counseling-agreement-template.md", "Agreement template"),
        ("09-toolkit/08-invoice-template-germany.md", "Invoice template"),
        ("09-toolkit/09-instagram-posts-counseling.md", "IG counseling posts"),
        ("09-toolkit/10-instagram-posts-coaching.md", "IG coaching posts"),
        ("09-toolkit/11-tiktok-script-batch.md", "TikTok scripts"),
        ("09-toolkit/12-newsletter-templates.md", "Newsletter templates"),
        ("09-toolkit/13-blog-post-batch.md", "Blog drafts"),
        ("09-toolkit/14-multilingual-adaptations.md", "Multilingual"),
    ]),
]

def slugify(text: str) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s]+", "-", s).strip("-") or "section"


def md_to_html_path(md_rel: str) -> str:
    if md_rel.startswith("../"):
        return "readme.html"
    return Path(md_rel).with_suffix(".html").as_posix()


def rel_link(from_html: str, to_html: str) -> str:
    """Relative URL from one generated page to another within site/."""
    from_dir = PurePosixPath(from_html).parent
    to_path = PurePosixPath(to_html)
    rel = os.path.relpath(to_path, from_dir if str(from_dir) != "." else "")
    return rel.replace("\\", "/")


def rel_prefix(html_path: str) -> str:
    depth = html_path.count("/")
    return "../" * depth if depth else ""


def normalize_posix(path: str) -> str:
    parts: list[str] = []
    for part in path.replace("\\", "/").split("/"):
        if part == "..":
            if parts:
                parts.pop()
        elif part and part != ".":
            parts.append(part)
    return "/".join(parts)


def rewrite_links(body_html: str, current_html: str, md_rel: str) -> str:
    md_dir = PurePosixPath(md_rel).parent

    def repl_href(m: re.Match) -> str:
        url = m.group(1)
        if url.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        if url.endswith(".md"):
            if "README" in Path(url).name.upper():
                return f'href="{rel_link(current_html, "readme.html")}"'
            if "brand/" in url:
                depth = current_html.count("/")
                idx = url.find("brand/")
                brand_path = url[idx:]
                return f'href="{("../" * (depth + 2))}{brand_path}"'
            if url.startswith("docs/"):
                html_target = str(Path(url.removeprefix("docs/")).with_suffix(".html"))
                return f'href="{rel_link(current_html, html_target)}"'
            target = normalize_posix(str(md_dir / url))
            html_target = str(Path(target).with_suffix(".html"))
            return f'href="{rel_link(current_html, html_target)}"'
        if url.startswith("site/"):
            return f'href="{rel_link(current_html, url.removeprefix("site/"))}"'
        if current_html == "readme.html" and url.startswith("../"):
            return f'href="{("../" * 1)}{url}"'
        return m.group(0)

    return re.sub(r'href="([^"]+)"', repl_href, body_html)


def add_heading_ids(body_html: str) -> tuple[str, list[tuple[str, str, int]]]:
    toc: list[tuple[str, str, int]] = []
    counter: dict[str, int] = {}

    def repl(m: re.Match) -> str:
        level = int(m.group(1))
        text = re.sub(r"<[^>]+>", "", m.group(2))
        base = slugify(text)
        counter[base] = counter.get(base, 0) + 1
        hid = base if counter[base] == 1 else f"{base}-{counter[base]}"
        if level in (2, 3):
            toc.append((hid, text, level))
        return f'<h{level} id="{hid}">{m.group(2)}</h{level}>'

    updated = re.sub(r"<h([23])>(.*?)</h\1>", repl, body_html, flags=re.DOTALL)
    return updated, toc


def mermaidify(body_html: str) -> str:
    def repl(m: re.Match) -> str:
        code = html.unescape(m.group(1))
        return f'<pre class="mermaid">{code.strip()}</pre>'

    return re.sub(
        r'<pre><code class="language-mermaid">(.*?)</code></pre>',
        repl,
        body_html,
        flags=re.DOTALL,
    )


def render_md(text: str) -> str:
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "nl2br", "sane_lists"],
        extension_configs={"fenced_code": {"lang_prefix": "language-"}},
    )
    return md.convert(text)


def card_dashboard_href(current_html: str) -> str:
    depth = current_html.count("/")
    return "../" * (depth + 1) + "index.html"


def build_sidebar(current_html: str) -> str:
    prefix = rel_prefix(current_html)
    groups: list[str] = []

    dash_active = ' class="is-active"' if current_html == "index.html" else ""
    groups.append(
        '<div class="suite-nav-group">'
        '<p class="suite-nav-group__label">Dashboard</p><ul>'
        f'<li><a href="{rel_link(current_html, "index.html")}"{dash_active}>Suite home</a></li>'
        f'<li><a href="{card_dashboard_href(current_html)}">Card dashboard</a></li>'
        "</ul></div>"
    )

    for _id, label, items in SECTIONS:
        links = []
        for md_path, title in items:
            href = md_to_html_path(md_path)
            active = ' class="is-active"' if href == current_html else ""
            links.append(
                f'<li><a href="{rel_link(current_html, href)}"{active}>{html.escape(title)}</a></li>'
            )
        groups.append(
            f'<div class="suite-nav-group">'
            f'<p class="suite-nav-group__label">{html.escape(label)}</p>'
            f'<ul>{"".join(links)}</ul></div>'
        )
    return "\n".join(groups)


def build_toc(toc: list[tuple[str, str, int]]) -> str:
    if len(toc) < 3:
        return ""
    items = []
    for hid, text, level in toc:
        cls = "toc-h3" if level == 3 else ""
        items.append(
            f'<li class="{cls}"><a href="#{hid}">{html.escape(text)}</a></li>'
        )
    return (
        '<aside class="suite-toc" aria-label="On this page">'
        '<p class="suite-toc__title">On this page</p>'
        f'<ul>{"".join(items)}</ul></aside>'
    )


def brand_prefix(html_path: str) -> str:
    depth = html_path.count("/")
    return "../" * (depth + 2)


def page_html(title: str, body: str, current_html: str, source_note: str, toc_html: str) -> str:
    prefix = rel_prefix(current_html)
    brand_depth = brand_prefix(current_html)
    has_mermaid = 'class="mermaid"' in body
    mermaid_script = ""
    if has_mermaid:
        mermaid_script = """
    <script type="module">
      import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
      const dark = document.documentElement.getAttribute("data-theme") === "dark"
        || (!document.documentElement.getAttribute("data-theme")
            && window.matchMedia("(prefers-color-scheme: dark)").matches);
      mermaid.initialize({ startOnLoad: true, theme: dark ? "dark" : "neutral" });
    </script>"""

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(title)} - Anna Hellmuth Business Suite</title>
  <script>(function(){{try{{var t=localStorage.getItem("suite-theme");if(t==="dark"||t==="light")document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}}})();</script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="{brand_depth}brand/tokens.css" />
  <link rel="stylesheet" href="{brand_depth}brand/typography.css" />
  <link rel="stylesheet" href="{prefix}assets/styles.css" />
</head>
<body class="suite-shell">
  <button type="button" class="suite-mobile-toggle" aria-label="Toggle navigation" id="nav-toggle">Menu</button>
  <aside class="suite-sidebar" id="sidebar">
    <a class="suite-brand" href="{rel_link(current_html, "index.html")}">
      <p class="suite-brand__name">Anna Hellmuth</p>
      <p class="suite-brand__sub">Business suite · internal operating manual</p>
    </a>
    {build_sidebar(current_html)}
    <div class="suite-sidebar__links">
      <a href="{brand_depth}index.html">Marketing Center</a>
      <a href="https://annahellmuth.com/" target="_blank" rel="noopener">annahellmuth.com</a>
    </div>
  </aside>
  <div class="suite-main">
    <div class="suite-toolbar">
      <a href="{rel_link(current_html, "index.html")}">← Dashboard</a>
      <button type="button" id="theme-toggle" aria-label="Toggle theme">Theme</button>
    </div>
    <div class="suite-content-wrap">
      <article class="suite-prose">
        {body}
        <footer class="suite-footer">Generated from <code>{html.escape(source_note)}</code> · Anna Hellmuth business suite</footer>
      </article>
      {toc_html}
    </div>
  </div>
  <script>
    (function() {{
      var btn = document.getElementById("theme-toggle");
      if (btn) btn.addEventListener("click", function() {{
        var root = document.documentElement;
        var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
        root.setAttribute("data-theme", next);
        try {{ localStorage.setItem("suite-theme", next); }} catch (e) {{}}
        location.reload();
      }});
      var toggle = document.getElementById("nav-toggle");
      var sidebar = document.getElementById("sidebar");
      if (toggle && sidebar) toggle.addEventListener("click", function() {{
        sidebar.classList.toggle("is-open");
      }});
    }})();
  </script>{mermaid_script}
</body>
</html>"""


def build_page(md_path: Path, html_rel: str) -> None:
    text = md_path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else md_path.stem

    body = render_md(text)
    body = mermaidify(body)
    body, toc = add_heading_ids(body)
    if md_path.resolve() == README.resolve():
        md_rel = "../README.md"
        source_note = "README.md"
    else:
        md_rel = str(md_path.relative_to(DOCS))
        source_note = f"docs/{html_rel.replace('.html', '.md')}"

    body = rewrite_links(body, html_rel, md_rel)

    toc_html = build_toc(toc)
    page = page_html(title, body, html_rel, source_note, toc_html)

    out = SITE / html_rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")


def main() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()
    shutil.copytree(ASSETS_SRC, SITE / "assets")

    md_files = sorted(DOCS.rglob("*.md"))
    print(f"Building {len(md_files)} pages…")

    for md_path in md_files:
        rel = md_path.relative_to(DOCS)
        html_rel = rel.with_suffix(".html").as_posix()
        build_page(md_path, html_rel)
        print(f"  {html_rel}")

    # README as readme.html at site root
    if README.exists():
        build_page(README, "readme.html")
        print("  readme.html")

    # Copy dashboard index - link to site from parent; also write a site index redirect note
    site_index = SITE / "index.html"
    dashboard_src = ROOT / "index.html"
    if dashboard_src.exists():
        # Write a simple redirect page to parent dashboard OR embed link
        site_index.write_text(
            f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="refresh" content="0; url=00-overview.html" />
  <title>Business Suite</title>
</head>
<body>
  <p><a href="00-overview.html">Open the business suite</a></p>
</body>
</html>""",
            encoding="utf-8",
        )

    print(f"\nDone → {SITE}/")
    print("Preview: python3 -m http.server 4173  (open /business-site/site/00-overview.html)")


if __name__ == "__main__":
    main()
