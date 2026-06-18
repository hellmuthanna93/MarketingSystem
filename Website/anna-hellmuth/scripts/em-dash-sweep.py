#!/usr/bin/env python3
"""Remove em/en dashes from website source copy. Skips testimonial blocks and cite attributions."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "src" / "locales"
MANIFEST = ROOT / "src" / "pages-manifest.yaml"

CITE_ATTRIBUTION = re.compile(
    r"[—–]\s*(Former client|Ehemalige Klientin|Carl Gustav Jung|Steve Biddulph)",
    re.IGNORECASE,
)

PHRASE_REPLACEMENTS = [
    (r" — and ", ", and "),
    (r" — but ", ", but "),
    (r" — or ", ", or "),
    (r" — including ", ", including "),
    (r" — no obligation", ", no obligation"),
    (r" — wherever ", ", wherever "),
    (r" — typically ", ", typically "),
    (r" — always ", ", always "),
    (r" — not just ", ", not just "),
    (r" — in sequence", ", in sequence"),
    (r" — from ", ", from "),
    (r" — auf ", ", auf "),
    (r"Erfüllung — Angebote", "Erfüllung: Angebote"),
    (r" — one ", ": one "),
    (r" — a sense ", ", a sense "),
    (r" — the sense ", ", the sense "),
    (r" — becoming ", ": becoming "),
    (r"potential—but", "potential, but"),
    (r"Witnessing — the", "Witnessing: the"),
    (r"countries — and", "countries and"),
    (r"aligned — from", "aligned, from"),
    (r"strength — until", "strength, until"),
    (r"Art\. 6 — typically", "Art. 6, typically"),
    (r"Anna Hellmuth — ", "Anna Hellmuth, "),
    (r" \| Reach Out To Me — Anna", " | Reach Out To Me | Anna"),
    (r"Legal Notice — Anna", "Legal Notice | Anna"),
    (r"Privacy Policy — Anna", "Privacy Policy | Anna"),
    (r"Datenschutzerklärung — Anna", "Datenschutzerklärung | Anna"),
    (r"Blog \| Anna Hellmuth — ", "Blog | Anna Hellmuth | "),
    (r" — ", ", "),
    (r"methods—a path", "methods, a path"),
    (r"myself—through", "myself: through"),
    (r"badly—now", "badly, now"),
    (r"level\)—fingers", "level). Fingers"),
]

EN_DASH_RANGE = re.compile(r"(\d+)–(\d+)")


def should_skip_line(line: str) -> bool:
    if CITE_ATTRIBUTION.search(line) and (
        "<cite" in line or "<span>" in line or "quote-author" in line
    ):
        return True
    return False


def replace_dashes_in_line(line: str) -> str:
    line = EN_DASH_RANGE.sub(r"\1-\2", line)
    for pattern, repl in PHRASE_REPLACEMENTS:
        line = re.sub(pattern, repl, line)
    if "—" in line or "–" in line:
        line = line.replace("—", ", ")
        line = line.replace("–", ", ")
    line = re.sub(r"([^ ])  +", r"\1 ", line)
    line = re.sub(r", ,", ",", line)
    return line


def process_text(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    in_testimonials = False
    section_depth = 0

    for line in lines:
        if 'id="testimonials"' in line:
            in_testimonials = True
            section_depth = 0

        if in_testimonials:
            out.append(line)
            section_depth += line.count("<section")
            section_depth -= line.count("</section>")
            if section_depth <= 0 and "</section>" in line:
                in_testimonials = False
            continue

        if should_skip_line(line):
            out.append(line)
            continue

        out.append(replace_dashes_in_line(line))

    return "".join(out)


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = process_text(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed: list[str] = []

    for path in sorted(LOCALES.rglob("*.j2")):
        if process_file(path):
            changed.append(str(path.relative_to(ROOT)))

    if MANIFEST.exists():
        original = MANIFEST.read_text(encoding="utf-8")
        updated = original
        for pattern, repl in [
            (r" \| Reach Out To Me — Anna", " | Reach Out To Me | Anna"),
            (r"Legal Notice — Anna", "Legal Notice | Anna"),
            (r"Privacy Policy — Anna", "Privacy Policy | Anna"),
            (r"Datenschutzerklärung — Anna", "Datenschutzerklärung | Anna"),
            (r"Blog \| Anna Hellmuth — ", "Blog | Anna Hellmuth | "),
            (r"Політика конфіденційності — ", "Політика конфіденційності | "),
            (r"Политика конфиденциальности — ", "Политика конфиденциальности | "),
        ]:
            updated = re.sub(pattern, repl, updated)
        if updated != original:
            MANIFEST.write_text(updated, encoding="utf-8")
            changed.append(str(MANIFEST.relative_to(ROOT)))

    print(f"Updated {len(changed)} files")
    for name in changed:
        print(f"  {name}")


if __name__ == "__main__":
    main()
