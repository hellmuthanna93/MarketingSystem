#!/usr/bin/env python3
"""Generate localized body templates from EN + translation tables."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN_BODIES = ROOT / "src" / "locales" / "en" / "bodies"

# Per-locale, per-body-file replacement maps (adapted copy, not literal translation)
TRANSLATIONS: dict[str, dict[str, dict[str, str]]] = {
    "de": {
        "contact.html.j2": {
            "<h1>Contact</h1>": "<h1>Kontakt</h1>",
            "Start your journey of transformation today.": "Starten Sie Ihre Veränderung heute.",
            "Reach Out": "Schreiben Sie mir",
            "For any inquiries, feel free to reach out to me here.": "Bei Fragen erreichen Sie mich hier.",
            "If you're ready to start working immediately, go ahead and message me about purchasing a single session or one of the packages.": "Wenn Sie direkt starten möchten, schreiben Sie mir zu einer Einzelsitzung oder einem Paket.",
            "Email": "E-Mail",
            "Nuremberg Office": "Büro Nürnberg",
            "Erhardstraße 13, 90482 Nuremberg, Germany": "Erhardstraße 13, 90482 Nürnberg, Deutschland",
            "1:1 Intake Consultation": "Kostenloses Erstgespräch",
            "If you're interested in 1:1 coaching or counseling sessions and have questions, let's connect for a brief 30-minute introductory call.": "Wenn Sie Fragen zu Einzelberatung oder Coaching haben, vereinbaren wir ein kurzes 30-minütiges Gespräch.",
            "Our introductory intake call is completely free of charge and helps us determine if our services align with your development goals.": "Das Erstgespräch ist kostenlos und klärt, ob mein Angebot zu Ihren Zielen passt.",
            "Select your slot": "Termin wählen",
            "Select a date and time directly below to schedule our free 30-minute introductory call.": "Wählen Sie unten Datum und Uhrzeit für unser kostenloses 30-minütiges Erstgespräch.",
            'title="Schedule a free 30-minute discovery call with Anna Hellmuth"': 'title="Kostenloses Erstgespräch mit Anna Hellmuth vereinbaren"',
        },
        "blog.html.j2": {
            "Insights for creative &amp; ambitious souls": "Gedanken für sensible, nachdenkliche Menschen",
            "Thoughts on emotional healing, bold goals, and the inner work behind a life that feels aligned — from psychological counseling and life coaching practice.": "Über emotionale Heilung, mutige Ziele und die innere Arbeit hinter einem Leben, das sich stimmig anfühlt.",
            "Counseling &amp; coaching": "Beratung &amp; Coaching",
            "Counseling vs life coaching: how to know what you need": "Beratung vs. Life Coaching: Was Sie wirklich brauchen",
            "You are functioning on the outside but unsure whether you need healing, direction, or both. A simple framework to choose the right kind of support.": "Außen funktionieren, innen unsicher: Heilung, Richtung oder beides? Ein einfacher Rahmen für die richtige Unterstützung.",
            "Online counseling": "Online-Beratung",
            "Online counseling when you live between countries — and languages": "Online-Beratung zwischen Ländern und Sprachen",
            "Therapy that follows you home, meets you in English, German, Ukrainian, or Russian, and understands what displacement does to the nervous system.": "Beratung, die Sie in EN, DE, UK oder RU begleitet und versteht, was Displacement mit dem Nervensystem macht.",
            "Psychological counseling": "Psychologische Beratung",
            "When success on the outside does not match how you feel inside": "Wenn äußerer Erfolg sich innen leer anfühlt",
            "Burnout is not laziness. For many high achievers, it is the body refusing to keep performing a life that no longer fits.": "Burnout ist keine Faulheit. Bei Leistungsträgern verweigert oft der Körper, ein zu teures Leben weiter zu tragen.",
            "Getting started": "Erste Schritte",
            "Signs you are carrying more than you should have to alone": "Anzeichen, dass Sie mehr tragen, als Sie allein sollten",
            "Self-reliance is a strength — until it becomes the reason you never let anyone help. How to tell when professional support would save you years.": "Selbstständigkeit ist Stärke, bis sie der Grund wird, niemanden zuzulassen. Wann professionelle Unterstützung Jahre spart.",
            "8 min read": "8 Min. Lesezeit",
            "7 min read": "7 Min. Lesezeit",
            "9 min read": "9 Min. Lesezeit",
            "6 min read": "6 Min. Lesezeit",
            "Not sure where to start?": "Nicht sicher, wo Sie anfangen sollen?",
            "A free 30-minute discovery call is a chance to ask questions, share what you are facing, and see whether counseling or coaching is the right fit.": "Ein kostenloses 30-minütiges Erstgespräch: Fragen stellen, teilen, was Sie bewegt, und klären, ob Beratung oder Coaching passt.",
        },
        "home.html.j2": {
            "Knowledge alone is not the same as real change.": "Wissen allein ist nicht dasselbe wie echte Veränderung.",
            "Online psychological counseling and life coaching, wherever you are, in English, German, Ukrainian, Russian, or a mix of them all": "Online psychologische Beratung und Life Coaching, auf Englisch, Deutsch, Ukrainisch, Russisch oder gemischt",
            "My services": "Meine Angebote",
            "From navigating life's difficulties to striving for greater fulfillment, I provide options designed to support your unique path": "Vom Umgang mit Lebenskrise bis zu mehr Erfüllung: Angebote für Ihren Weg",
            "Psychological counseling": "Psychologische Beratung",
            "Find your power to release emotional burdens and heal your soul": "Emotionale Lasten lösen und innere Heilung finden",
            "Discover Counseling Services": "Zur psychologischen Beratung",
            "Life coaching": "Life Coaching",
            "Realize your ambitious goals and ascend to new heights": "Ambitionierte Ziele verwirklichen und neue Höhen erreichen",
            "Explore Coaching Details": "Zum Life Coaching",
            "What my clients are saying about working with me": "Was Klientinnen und Klienten über die Arbeit mit mir sagen",
            "* feedback from clients is posted anonymously to protect their privacy": "* Rückmeldungen werden anonym veröffentlicht, um die Privatsphäre zu schützen",
            "— Former client*": "— Ehemalige Klientin/Klient*",
            "Starting your journey toward a new life is easy": "Der Einstieg in ein neues Leben ist einfach",
            "<strong>Step 1:</strong> Schedule a free 30-minute intake call.": "<strong>Schritt 1:</strong> Kostenloses 30-minütiges Erstgespräch vereinbaren.",
            "<strong>Step 2:</strong> During the call, ask any questions and see if we resonate.": "<strong>Schritt 2:</strong> Fragen stellen und prüfen, ob wir zusammenpassen.",
            "<strong>Step 3:</strong> If we both agree that my services are a good fit for you, we begin your transformation journey.": "<strong>Schritt 3:</strong> Wenn es passt, beginnen wir Ihre Veränderungsreise.",
            "A free 30-minute session with me is an opportunity for you to…": "Ein kostenloses 30-minütiges Gespräch mit mir ist eine Gelegenheit…",
            "Frequently asked questions": "Häufig gestellte Fragen",
            "Get to know me": "Lernen Sie mich kennen",
            "Select a date and time directly below to schedule our free 30-minute introductory call.": "Wählen Sie unten Datum und Uhrzeit für unser kostenloses Erstgespräch.",
            "View on Instagram": "Auf Instagram ansehen",
        },
        "counseling.html.j2": {
            "The way you feel today is not the way you will feel forever.": "So wie Sie sich heute fühlen, werden Sie sich nicht immer fühlen.",
            "Learn more about me and my methods": "Mehr über mich und meine Methoden",
            "These are the challenges a lot of us are dealing with": "Diese Herausforderungen kennen viele von uns",
            "Your investment in yourself": "Ihre Investition in sich selbst",
            "What to expect from counselling with me": "Was Sie bei der Beratung mit mir erwartet",
            "Single Session": "Einzelsitzung",
            "Counseling Package": "Beratungspaket",
            "Recommended": "Empfohlen",
        },
        "lifecoaching.html.j2": {
            "Schedule your discovery call": "{{ site.cta }}",
        },
        "blog-counseling-vs-coaching.html.j2": {
            "Counseling vs life coaching: how to know what you need": "Beratung vs. Life Coaching: Was Sie wirklich brauchen",
            "Schedule your discovery call": "{{ site.cta }}",
        },
        "blog-expats.html.j2": {
            "Online counseling when you live between countries — and languages": "Online-Beratung zwischen Ländern und Sprachen",
            "Why language matters in therapy": "Warum Sprache in der Beratung zählt",
        },
        "blog-burnout.html.j2": {
            "When success on the outside does not match how you feel inside": "Wenn äußerer Erfolg sich innen leer anfühlt",
            "Burnout is not laziness": "Burnout ist keine Faulheit",
        },
        "blog-signs.html.j2": {
            "Signs you are carrying more than you should have to alone": "Anzeichen, dass Sie mehr tragen, als Sie allein sollten",
        },
    },
    "uk": {
        "contact.html.j2": {
            "<h1>Contact</h1>": "<h1>Контакт</h1>",
            "Start your journey of transformation today.": "Почніть свою подорож змін сьогодні.",
            "Reach Out": "Зв'яжіться зі мною",
            "For any inquiries, feel free to reach out to me here.": "З усіх питань пишіть мені тут.",
            "Email": "Електронна пошта",
            "Nuremberg Office": "Офіс у Нюрнберзі",
            "Erhardstraße 13, 90482 Nuremberg, Germany": "Erhardstraße 13, 90482 Нюрнберг, Німеччина",
            "1:1 Intake Consultation": "Безкоштовна ознайомлювальна зустріч",
            "Select your slot": "Оберіть час",
        },
        "blog.html.j2": {
            "Insights for creative &amp; ambitious souls": "Думки для чутливих, вдумливих людей",
            "Not sure where to start?": "Не знаєте, з чого почати?",
        },
        "home.html.j2": {
            "Knowledge alone is not the same as real change.": "Знання саме по собі, це не те саме, що справжня зміна.",
            "My services": "Мої послуги",
            "Psychological counseling": "Психологічне консультування",
            "Life coaching": "Лайф-коучинг",
            "Frequently asked questions": "Часті запитання",
            "Get to know me": "Познайомтеся зі мною",
        },
        "blog-counseling-vs-coaching.html.j2": {
            "Counseling vs life coaching: how to know what you need": "Консультування чи лайф-коучинг: що вам потрібно",
        },
        "blog-expats.html.j2": {
            "Online counseling when you live between countries — and languages": "Онлайн-консультування між країнами і мовами",
            "Why language matters in therapy": "Чому мова важлива в терапії",
        },
    },
    "ru": {
        "contact.html.j2": {
            "<h1>Contact</h1>": "<h1>Контакт</h1>",
            "Start your journey of transformation today.": "Начните свой путь изменений сегодня.",
            "Reach Out": "Свяжитесь со мной",
            "For any inquiries, feel free to reach out to me here.": "По любым вопросам пишите мне здесь.",
            "Email": "Электронная почта",
            "Nuremberg Office": "Офис в Нюрнберге",
            "Erhardstraße 13, 90482 Nuremberg, Germany": "Erhardstraße 13, 90482 Нюрнберг, Германия",
            "1:1 Intake Consultation": "Бесплатная ознакомительная встреча",
            "Select your slot": "Выберите время",
        },
        "blog.html.j2": {
            "Insights for creative &amp; ambitious souls": "Мысли для чувствительных, вдумчивых людей",
            "Not sure where to start?": "Не знаете, с чего начать?",
        },
        "home.html.j2": {
            "Knowledge alone is not the same as real change.": "Знания сами по себе, это не то же самое, что настоящие изменения.",
            "My services": "Мои услуги",
            "Psychological counseling": "Психологическое консультирование",
            "Life coaching": "Лайф-коучинг",
            "Frequently asked questions": "Частые вопросы",
            "Get to know me": "Познакомьтесь со мной",
        },
        "blog-counseling-vs-coaching.html.j2": {
            "Counseling vs life coaching: how to know what you need": "Консультирование или лайф-коучинг: что вам нужно",
        },
        "blog-expats.html.j2": {
            "Online counseling when you live between countries — and languages": "Онлайн-консультирование между странами и языками",
            "Why language matters in therapy": "Почему язык важен в терапии",
        },
    },
}


def apply(text: str, mapping: dict[str, str]) -> str:
    for old, new in sorted(mapping.items(), key=lambda x: -len(x[0])):
        text = text.replace(old, new)
    return text


LOCALE_ONLY_BODIES = {
    "de": {"impressum.html.j2", "privacy-policy.html.j2"},
    "uk": {"impressum.html.j2", "privacy-policy.html.j2"},
    "ru": {"impressum.html.j2", "privacy-policy.html.j2"},
    "en": {"impressum.html.j2", "privacy-policy.html.j2"},
}


def main() -> None:
    for locale, files in TRANSLATIONS.items():
        dest_dir = ROOT / "src" / "locales" / locale / "bodies"
        dest_dir.mkdir(parents=True, exist_ok=True)
        skip = LOCALE_ONLY_BODIES.get(locale, set())
        for fname in EN_BODIES.glob("*.html.j2"):
            if fname.name in skip:
                continue
            text = fname.read_text(encoding="utf-8")
            if fname.name in files:
                text = apply(text, files[fname.name])
            (dest_dir / fname.name).write_text(text, encoding="utf-8")
        print(f"Updated {locale} bodies")


if __name__ == "__main__":
    main()
