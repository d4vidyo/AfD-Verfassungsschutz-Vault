---
type: zitat
speaker: "[[Jörg Dornau]]"
date: 2021-11-20
topic: Menschenwürde
page_bfv: 466
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Dornau]] vom 20.11.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Kretschmer und Köpping verbieten unsere Weihnachtsmärkte während täglich neue Invasoren aus Islamischen Ländern einfallen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 466

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