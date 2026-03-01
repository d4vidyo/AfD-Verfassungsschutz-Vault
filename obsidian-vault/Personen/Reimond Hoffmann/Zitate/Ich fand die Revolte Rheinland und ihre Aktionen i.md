---
type: zitat
speaker: "[[Reimond Hoffmann]]"
date: 2023-12-18
topic: Sonstiges
page_bfv: 791
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Reimond Hoffmann]] vom 18.12.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ich fand die Revolte Rheinland und ihre Aktionen immer sehr gut bisher. Eine öffentliche Unvereinbarkeit, die diesen mutigen jungen Leuten in den Rücken fällt halte ich für überflüssig.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 791

**Verfassungsschutz Kategorisierung:** Sonstiges.

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