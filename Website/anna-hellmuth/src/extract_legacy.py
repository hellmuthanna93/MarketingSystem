#!/usr/bin/env python3
"""Extract <main> content from legacy HTML into EN body templates."""

from __future__ import annotations

import posixpath
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "src" / "locales" / "en" / "bodies"

MAPPING = {
    "index.html": "home.html.j2",
    "counseling.html": "counseling.html.j2",
    "lifecoaching.html": "lifecoaching.html.j2",
    "about.html": "about.html.j2",
    "contact.html": "contact.html.j2",
    "impressum.html": "impressum.html.j2",
    "privacy-policy.html": "privacy-policy.html.j2",
    "blog/index.html": "blog.html.j2",
    "blog/counseling-vs-life-coaching.html": "blog-counseling-vs-coaching.html.j2",
    "blog/online-counseling-for-expats.html": "blog-expats.html.j2",
    "blog/burnout-when-success-feels-empty.html": "blog-burnout.html.j2",
    "blog/signs-you-need-professional-support.html": "blog-signs.html.j2",
}

PAGE_KEYS = {
    "index.html": "home",
    "counseling.html": "counseling",
    "lifecoaching.html": "lifecoaching",
    "about.html": "about",
    "contact.html": "contact",
    "impressum.html": "impressum",
    "privacy-policy.html": "privacy-policy",
    "blog/index.html": "blog",
    "blog/counseling-vs-life-coaching.html": "blog-counseling-vs-coaching",
    "blog/online-counseling-for-expats.html": "blog-expats",
    "blog/burnout-when-success-feels-empty.html": "blog-burnout",
    "blog/signs-you-need-professional-support.html": "blog-signs",
}

BLOG_SLUGS = {
    "counseling-vs-life-coaching": "blog-counseling-vs-coaching",
    "online-counseling-for-expats": "blog-expats",
    "burnout-when-success-feels-empty": "blog-burnout",
    "signs-you-need-professional-support": "blog-signs",
}


def extract_main(html: str) -> str:
    m = re.search(r"<main[^>]*>(.*)</main>", html, re.DOTALL | re.IGNORECASE)
    if not m:
        raise ValueError("No <main> found")
    return m.group(1).strip()


def transform_body(body: str, is_blog: bool) -> str:
    body = re.sub(r'src="assets/([^"]+)"', r'src="{{ asset(\'\1\') }}"', body)
    body = re.sub(r"url\('assets/([^']+)'\)", r"url('{{ asset('\1') }}')", body)

    def repl_href(match: re.Match[str]) -> str:
        href = match.group(1)
        if href.startswith("#") or href.startswith("http") or href.startswith("mailto:"):
            return match.group(0)
        if href.startswith("../"):
            inner = href.replace("../", "")
            if inner.startswith("blog/"):
                slug = inner.replace("blog/", "").replace(".html", "")
                key = BLOG_SLUGS.get(slug, slug)
                return f'href="{{{{ page_url(\'{key}\') }}}}"'
            key = PAGE_KEYS.get(inner, inner.replace(".html", ""))
            return f'href="{{{{ page_url(\'{key}\') }}}}"'
        if href.startswith("blog/"):
            slug = href.replace("blog/", "").replace(".html", "")
            key = BLOG_SLUGS.get(slug, slug)
            return f'href="{{{{ page_url(\'{key}\') }}}}"'
        key = PAGE_KEYS.get(href, href.replace(".html", ""))
        if key == "index":
            key = "home"
        return f'href="{{{{ page_url(\'{key}\') }}}}"'

    body = re.sub(r'href="([^"]+)"', repl_href, body)
    body = body.replace("Schedule your discovery call", "{{ site.cta }}")
    return body


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for src_rel, out_name in MAPPING.items():
        src = ROOT / src_rel
        html = src.read_text(encoding="utf-8")
        body = transform_body(extract_main(html), is_blog="blog/" in src_rel)
        (OUT / out_name).write_text(body + "\n", encoding="utf-8")
        print(f"Wrote {out_name}")


if __name__ == "__main__":
    main()
