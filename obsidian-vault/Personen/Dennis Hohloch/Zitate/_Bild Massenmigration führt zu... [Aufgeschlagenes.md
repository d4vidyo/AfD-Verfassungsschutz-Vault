---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2023-05-25
topic: Menschenwürde
page_bfv: 394
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 25.5.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>\<Bild Massenmigration führt zu... [Aufgeschlagenes Buch] massenhaftem Analphabetismus [Krankenhaus-Symbol] höheren Krankenkassenbeiträgen [Lehrer-Symbol] verschärftem Lehrermangel [Haus-Symbol] Wohnungsnotstand [Messer-Symbol] höherer Kriminalität [Blutstropfen-Symbol] mehr Morden & Vergewaltigungen [Geld-Symbol] höheren Steuern Massenabschiebungen führen ins Gegenteil.\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 394

**Verfassungsschutz Kategorisierung:** Verstoß gegen die Menschenwürde.

---
## Meine Auswertung:

**Meine Bewertung:** `INPUT[inlineSelect(option(Unbewertet), option(Legitim), option(Fragwürdig), option(Nicht legitim), defaultValue(Unbewertet)):status]`

_Mein Kommentar:_ 


---
# Nächste Aussage:
```dataview
TABLE speaker AS "Person", date AS "Datum", topic AS "Thema", choice(speaker.is_still_member, "Ja", "Nein") AS "Noch Mitglied?"
FROM "Personen"
WHERE type = "zitat" and status = "Unbewertet" AND file.name != this.file.name
SORT speaker.is_still_member DESC, speaker.relevance ASC, speaker ASC, date ASC
LIMIT 10
```