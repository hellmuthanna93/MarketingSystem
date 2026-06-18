#!/usr/bin/env python3
"""
Build multilingual static site from src/ templates and locale bodies.

Usage:
  python3 build-website.py
  python3 build-website.py --locale en

Source: src/  ·  Output: en/, de/, uk/, ru/ (+ root index.html, sitemap.xml)
Do not hand-edit generated HTML.
"""

from __future__ import annotations

import argparse
import posixpath
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
TEMPLATES = SRC / "templates"
LOCALES_DIR = SRC / "locales"
MANIFEST_PATH = SRC / "pages-manifest.yaml"
SITE_URL = "https://annahellmuth.com"
PAGE_KEY_ALIASES = {
    "index": "home",
    "counseling-vs-life-coaching": "blog-counseling-vs-coaching",
    "online-counseling-for-expats": "blog-expats",
    "burnout-when-success-feels-empty": "blog-burnout",
    "signs-you-need-professional-support": "blog-signs",
}
LOCALE_CODES = ("en", "de", "uk", "ru")


@dataclass
class PageDef:
    translation_key: str
    category: str
    slugs: dict[str, str]
    titles: dict[str, str]
    descriptions: dict[str, str]

    def slug(self, locale: str) -> str:
        return self.slugs[locale]

    def title(self, locale: str) -> str:
        return self.titles.get(locale, self.titles["en"])

    def description(self, locale: str) -> str:
        return self.descriptions.get(locale, self.descriptions.get("en", ""))


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_manifest() -> tuple[list[PageDef], list[str]]:
    data = load_yaml(MANIFEST_PATH)
    pages = []
    for p in data["pages"]:
        pages.append(
            PageDef(
                translation_key=p["translation_key"],
                category=p["category"],
                slugs=p["slugs"],
                titles=p["titles"],
                descriptions=p.get("descriptions", {}),
            )
        )
    return pages, data.get("locales", list(LOCALE_CODES))


def build_url_index(pages: list[PageDef], locales: list[str]) -> dict[str, dict[str, str]]:
    """translation_key -> locale -> site-relative path (no leading slash)."""
    index: dict[str, dict[str, str]] = {}
    for page in pages:
        index[page.translation_key] = {}
        for loc in locales:
            slug = page.slug(loc)
            if page.category == "blog-index":
                path = f"{loc}/blog/{slug}.html"
            elif page.category == "blog":
                path = f"{loc}/blog/{slug}.html"
            else:
                path = f"{loc}/{slug}.html"
            index[page.translation_key][loc] = path
    return index


class SiteBuilder:
    def __init__(self, locales: list[str] | None = None) -> None:
        self.pages, all_locales = load_manifest()
        self.locales = locales or all_locales
        self.contact = load_yaml(SRC / "shared" / "contact.yaml")
        self.pricing = load_yaml(SRC / "shared" / "pricing.yaml")
        self.url_index = build_url_index(self.pages, all_locales)
        self.site_configs: dict[str, dict] = {}
        for loc in all_locales:
            self.site_configs[loc] = load_yaml(LOCALES_DIR / loc / "site.yaml")
        self.env = Environment(
            loader=FileSystemLoader(str(TEMPLATES)),
            autoescape=select_autoescape(["html", "xml", "j2"]),
        )
        self.env.globals["site_url"] = SITE_URL

    def _depth(self, page: PageDef) -> int:
        return 1 if page.category in ("blog", "blog-index") else 0

    def _rel(self, page: PageDef, *parts: str) -> str:
        depth = self._depth(page)
        prefix = "../" * (depth + 1)
        return prefix + "/".join(parts)

    def asset(self, page: PageDef, path: str) -> str:
        return self._rel(page, "assets", path)

    def brand(self, page: PageDef, path: str) -> str:
        # locale dir (+1) + repo root from anna-hellmuth (+1) => depth + 3
        depth = self._depth(page)
        prefix = "../" * (depth + 3)
        return prefix + "brand/" + path

    def page_url(self, page: PageDef, locale: str, key: str) -> str:
        anchor = ""
        if "#" in key:
            key, anchor = key.split("#", 1)
            anchor = "#" + anchor
        key = PAGE_KEY_ALIASES.get(key, key)
        current_rel = self.url_index[page.translation_key][locale].split("/", 1)[1]
        target_rel = self.url_index[key][locale].split("/", 1)[1]
        current_dir = posixpath.dirname(current_rel) or "."
        return posixpath.relpath(target_rel, current_dir) + anchor

    def locale_href(self, page: PageDef, from_locale: str, to_locale: str) -> str:
        current_rel = self.url_index[page.translation_key][from_locale].split("/", 1)[1]
        target = self.url_index[page.translation_key][to_locale]
        ups = current_rel.count("/") + 1
        return ("../" * ups) + target

    def alternates(self, page: PageDef) -> list[dict[str, str]]:
        alts = []
        for loc in LOCALE_CODES:
            path = self.url_index[page.translation_key][loc]
            alts.append({"lang": loc, "href": f"{SITE_URL}/{path}"})
        alts.append({"lang": "x-default", "href": f"{SITE_URL}/{self.url_index[page.translation_key]['en']}"})
        return alts

    def canonical(self, page: PageDef, locale: str) -> str:
        return f"{SITE_URL}/{self.url_index[page.translation_key][locale]}"

    def language_links(self, page: PageDef, current_locale: str) -> list[dict[str, str]]:
        links = []
        for loc in LOCALE_CODES:
            cfg = self.site_configs[loc]
            if loc == current_locale:
                href = "#"
            else:
                href = self.locale_href(page, current_locale, loc)
            links.append(
                {
                    "code": loc,
                    "short": cfg["locale_short"],
                    "name": cfg["locale_name"],
                    "href": href,
                    "current": loc == current_locale,
                }
            )
        return links

    def load_body(self, locale: str, page: PageDef) -> str:
        key = page.translation_key
        body_map = {
            "home": "home",
            "blog": "blog",
        }
        fname = body_map.get(key, key.replace("blog-", "blog-")) + ".html.j2"
        if key == "home":
            fname = "home.html.j2"
        elif key.startswith("blog-"):
            fname = f"{key}.html.j2"
        elif key == "blog":
            fname = "blog.html.j2"
        else:
            fname = f"{key}.html.j2"

        path = LOCALES_DIR / locale / "bodies" / fname
        if not path.exists():
            raise FileNotFoundError(f"Missing body: {path}")
        template = self.env.from_string(path.read_text(encoding="utf-8"))
        ctx = self.render_context(locale, page)
        return template.render(**ctx)

    def render_context(self, locale: str, page: PageDef) -> dict[str, Any]:
        site = self.site_configs[locale]

        def asset(path: str) -> str:
            return self.asset(page, path)

        def page_url(key: str) -> str:
            return self.page_url(page, locale, key)

        return {
            "site": site,
            "contact": self.contact,
            "pricing": self.pricing,
            "page": page,
            "locale": locale,
            "asset": asset,
            "page_url": page_url,
            "current_key": page.translation_key,
        }

    def template_name(self, page: PageDef) -> str:
        if page.category == "legal":
            return "legal.html"
        if page.category == "blog-index":
            return "blog-index.html"
        if page.category == "blog":
            return "blog-article.html"
        return "page.html"

    def render_page(self, locale: str, page: PageDef) -> str:
        tpl = self.env.get_template(self.template_name(page))
        ctx = self.render_context(locale, page)
        ctx.update(
            {
                "title": page.title(locale),
                "meta_description": page.description(locale) or self.site_configs[locale]["meta_default_description"],
                "body_html": self.load_body(locale, page),
                "alternates": self.alternates(page),
                "canonical": self.canonical(page, locale),
                "language_links": self.language_links(page, locale),
                "nav_pages": self.pages,
                "url_index": self.url_index,
                "asset_path": lambda p: self.asset(page, p),
                "brand_path": lambda p: self.brand(page, p),
                "link_to": lambda key: self.page_url(page, locale, key),
                "is_active": lambda key: page.translation_key == key,
                "blog_css": page.category in ("blog", "blog-index"),
            }
        )
        return tpl.render(**ctx)

    def output_path(self, locale: str, page: PageDef) -> Path:
        slug = page.slug(locale)
        if page.category in ("blog", "blog-index"):
            return ROOT / locale / "blog" / f"{slug}.html"
        return ROOT / locale / f"{slug}.html"

    def clean_outputs(self) -> None:
        for loc in self.locales:
            loc_dir = ROOT / loc
            if loc_dir.exists():
                shutil.rmtree(loc_dir)
        for legacy in [
            "counseling.html",
            "lifecoaching.html",
            "about.html",
            "contact.html",
            "impressum.html",
            "privacy-policy.html",
        ]:
            p = ROOT / legacy
            if p.exists():
                p.unlink()
        blog_legacy = ROOT / "blog"
        if blog_legacy.exists():
            shutil.rmtree(blog_legacy)

    def write_root_redirect(self) -> None:
        html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=en/index.html">
  <link rel="canonical" href="https://annahellmuth.com/en/index.html">
  <title>Anna Hellmuth</title>
  <script>location.replace('en/index.html');</script>
</head>
<body>
  <p><a href="en/index.html">Continue to Anna Hellmuth</a></p>
</body>
</html>
"""
        (ROOT / "index.html").write_text(html, encoding="utf-8")

    def write_sitemap(self) -> None:
        urls = []
        for page in self.pages:
            for loc in LOCALE_CODES:
                urls.append(f"{SITE_URL}/{self.url_index[page.translation_key][loc]}")
        lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for u in sorted(urls):
            lines.append("  <url>")
            lines.append(f"    <loc>{u}</loc>")
            lines.append("  </url>")
        lines.append("</urlset>")
        (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")

    def write_redirects_doc(self) -> None:
        lines = ["# Legacy URL redirects (301)", "", "Configure on your host:", ""]
        legacy_map = {
            "index.html": "en/index.html",
            "counseling.html": "en/counseling.html",
            "lifecoaching.html": "en/lifecoaching.html",
            "about.html": "en/about.html",
            "contact.html": "en/contact.html",
            "impressum.html": "en/impressum.html",
            "privacy-policy.html": "en/privacy-policy.html",
            "blog/index.html": "en/blog/index.html",
            "blog/counseling-vs-life-coaching.html": "en/blog/counseling-vs-life-coaching.html",
            "blog/online-counseling-for-expats.html": "en/blog/online-counseling-for-expats.html",
            "blog/burnout-when-success-feels-empty.html": "en/blog/burnout-when-success-feels-empty.html",
            "blog/signs-you-need-professional-support.html": "en/blog/signs-you-need-professional-support.html",
        }
        for old, new in legacy_map.items():
            lines.append(f"/{old} → /{new}")
        (ROOT / "REDIRECTS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    def build(self) -> None:
        self.clean_outputs()
        for locale in self.locales:
            for page in self.pages:
                out = self.output_path(locale, page)
                out.parent.mkdir(parents=True, exist_ok=True)
                html = self.render_page(locale, page)
                out.write_text(html, encoding="utf-8")
                print(f"Built {out.relative_to(ROOT)}")
        self.write_root_redirect()
        self.write_sitemap()
        self.write_redirects_doc()
        print("Done.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", action="append", dest="locales")
    args = parser.parse_args()
    builder = SiteBuilder(locales=args.locales)
    builder.build()


if __name__ == "__main__":
    main()
