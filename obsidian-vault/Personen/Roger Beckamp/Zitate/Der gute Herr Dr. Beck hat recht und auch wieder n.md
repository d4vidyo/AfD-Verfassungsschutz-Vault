---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2022-06-08
topic: Menschenwürde
page_bfv: 376
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 8.6.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Der gute Herr Dr. Beck hat recht und auch wieder nicht. Er war wohl noch nie in Dortmund

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 376. Kommentar zu einem Repost

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