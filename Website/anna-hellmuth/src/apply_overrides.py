#!/usr/bin/env python3
"""Apply locale-specific string replacements to body templates."""

from __future__ import annotations

import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCALES = ("de", "uk", "ru")


def apply_replacements(text: str, pairs: list[dict[str, str]]) -> str:
    for pair in pairs:
        text = text.replace(pair["from"], pair["to"])
    return text


def main() -> None:
    for loc in LOCALES:
        overrides_dir = ROOT / "src" / "locales" / loc / "overrides"
        if not overrides_dir.exists():
            continue
        for override_file in sorted(overrides_dir.glob("*.yaml")):
            data = yaml.safe_load(override_file.read_text(encoding="utf-8"))
            body_name = data["body"]
            pairs = data.get("replacements", [])
            body_path = ROOT / "src" / "locales" / loc / "bodies" / body_name
            if not body_path.exists():
                print(f"SKIP missing body {body_path}")
                continue
            text = body_path.read_text(encoding="utf-8")
            text = apply_replacements(text, pairs)
            body_path.write_text(text, encoding="utf-8")
            print(f"Applied {override_file.name} -> {body_name}")


if __name__ == "__main__":
    main()
