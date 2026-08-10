# Invoice (Rechnung) - Germany Template

> **Not tax advice.** Anna currently applies the Kleinunternehmerregelung under
> §19 UStG, so block B is the working default and VAT is not added or shown
> separately. Recheck the wording with a Steuerberater if her status changes.
> Replace `{{placeholders}}`.

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
> Leistungszeitraum: {{TT.MM.JJJJ - TT.MM.JJJJ}}
>
> | Pos. | Beschreibung | Menge | Einzelpreis | Betrag |
> |------|--------------|-------|-------------|--------|
> | 1 | {{z. B. Psychologische Beratung, 60 Min.}} | {{1}} | €{{120,00}} | €{{120,00}} |
> | 2 | {{16-wöchiges 1:1-Coachingprogramm}} | {{1}} | €{{1.950,00}} | €{{1.950,00}} |
>
> {{- Choose ONE of the following blocks -}}
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
> Alternativ per Revolut-Überweisung an: {{Revolut-Zahlungsdaten}}
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
- [ ] Net amount + USt rate/amount - OR §19 note - OR §4 Nr. 14 exemption note
- [ ] Total amount
- [ ] Payment terms + bank and Revolut transfer details

## Notes

- Block B is the current default under Anna's Kleinunternehmer status. Recheck
  if her status changes; therapeutic and coaching services may be treated
  differently.
- Keep invoices per German retention rules (commonly up to 10 years).
- Use one consistent numbering scheme.

## So what

A fill-in invoice with the current §19 default and alternatives for a future
tax-status change. Part of the document set in
[../07-finance-legal/04-templates.md](../07-finance-legal/04-templates.md).
