---
type: zitat
speaker: "[[Harald Laatsch]]"
date: 2023-12-29
topic: Menschenwürde
page_bfv: 412
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Harald Laatsch]] vom 29.12.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Bei uns ist #Remigration schon lange Programm, was soll da neu sein?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 412

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