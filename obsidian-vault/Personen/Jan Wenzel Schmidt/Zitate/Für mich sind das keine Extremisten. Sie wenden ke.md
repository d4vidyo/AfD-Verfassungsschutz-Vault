---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2023-11-13
topic: Sonstiges
page_bfv: 783
source: 'Heimatkurier'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 13.11.2023 veröffentlicht auf: 'Heimatkurier'
> [!quote] Aussage
>Für mich sind das keine Extremisten. Sie wenden keine Gewalt an, um ihre politischen Ziele umzusetzen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 783

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