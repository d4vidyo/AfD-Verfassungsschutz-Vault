---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2025-01-08
topic: Demokratieprinzip
page_bfv: 952
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 8.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die Altparteien haben uns alles genommen: Heimat, Freiheit, Sicherheit. Die Kartellparteien sind unser Unglück

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 952

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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