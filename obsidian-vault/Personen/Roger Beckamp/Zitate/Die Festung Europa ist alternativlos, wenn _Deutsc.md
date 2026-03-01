---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2022-06-30
topic: Menschenwürde
page_bfv: 376
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 30.6.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Festung Europa ist alternativlos, wenn #Deutschland fortbestehen soll!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 376

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