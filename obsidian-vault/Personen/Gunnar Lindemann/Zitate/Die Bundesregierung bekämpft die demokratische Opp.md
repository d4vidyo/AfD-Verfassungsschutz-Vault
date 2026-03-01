---
type: zitat
speaker: "[[Gunnar Lindemann]]"
date: 2024-01-19
topic: Demokratieprinzip
page_bfv: 584
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Gunnar Lindemann]] vom 19.1.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die Bundesregierung bekämpft die demokratische Opposition. Wie in einer Diktatur.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 584

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