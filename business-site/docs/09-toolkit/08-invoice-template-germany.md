# Invoice (Rechnung) — Germany Template

> **Not tax advice.** A German-compliant invoice template per §14 UStG, with a §19 Kleinunternehmer variant. Confirm USt treatment per service with a Steuerberater ([../07-finance-legal/01-legal-setup-germany.md](../07-finance-legal/01-legal-setup-germany.md)). Replace `{{placeholders}}`.

---

## Template

> **Anna Hellmuth**
> {{Street, No.}}
> {{PLZ}} {{Stadt}}
> {{E-Mail}} · {{Telefon}}
> Steuernummer: {{Steuernummer}} {{/ USt-IdNr. if applicable}}
>
> ---
>
> **Rechnung**
>
> **An:**
> {{Kundenname}}
> {{Adresse}}
>
> Rechnungsnummer: {{fortlaufende Nr., z. B. 2026-014}}
> Rechnungsdatum: {{TT.MM.JJJJ}}
> Leistungszeitraum: {{TT.MM.JJJJ – TT.MM.JJJJ}}
>
> | Pos. | Beschreibung | Menge | Einzelpreis | Betrag |
> |------|--------------|-------|-------------|--------|
> | 1 | {{z. B. Psychologische Beratung, 60 Min.}} | {{1}} | €{{120,00}} | €{{120,00}} |
> | 2 | {{z. B. Coaching-Sitzung, 60 Min.}} | {{...}} | €{{...}} | €{{...}} |
>
> {{— Choose ONE of the following blocks —}}
>
> **A) Standard (USt-pflichtig):**
> Nettobetrag: €{{...}}
> zzgl. {{19}} % USt: €{{...}}
> **Gesamtbetrag: €{{...}}**
>
> **B) Kleinunternehmer (§19 UStG):**
> **Gesamtbetrag: €{{...}}**
> *Gemäß § 19 UStG wird keine Umsatzsteuer berechnet.*
>
> **C) Steuerfreie Heilbehandlung (where applicable, §4 Nr. 14 UStG):**
> **Gesamtbetrag: €{{...}}**
> *Umsatzsteuerfrei gemäß § 4 Nr. 14 UStG (Heilbehandlung).*
>
> ---
>
> Zahlbar bis {{TT.MM.JJJJ}} auf folgendes Konto:
> {{Kontoinhaber}} · IBAN {{...}} · BIC {{...}}
> Verwendungszweck: {{Rechnungsnummer}}
>
> Vielen Dank für Ihr Vertrauen.

---

## Required fields checklist (§14 UStG)

- [ ] Provider full name + address
- [ ] Client full name + address
- [ ] Steuernummer or USt-IdNr.
- [ ] Unique sequential invoice number
- [ ] Invoice date
- [ ] Service date / period
- [ ] Quantity + description of each service
- [ ] Net amount + USt rate/amount — OR §19 note — OR §4 Nr. 14 exemption note
- [ ] Total amount
- [ ] Payment terms + bank details

## Notes

- Which block (A/B/C) applies depends on Anna's USt status and whether a service qualifies as Heilbehandlung — **confirm with a Steuerberater**; therapeutic vs coaching portions may be treated differently.
- Keep invoices per German retention rules (commonly up to 10 years).
- Use one consistent numbering scheme.

## So what

A compliant, fill-in invoice with the three USt scenarios so Anna can bill correctly once her tax status is confirmed. Part of the document set in [../07-finance-legal/04-templates.md](../07-finance-legal/04-templates.md).
