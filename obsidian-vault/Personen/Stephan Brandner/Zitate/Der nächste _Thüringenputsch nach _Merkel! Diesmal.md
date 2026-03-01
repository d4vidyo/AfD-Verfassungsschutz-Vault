---
type: zitat
speaker: "[[Stephan Brandner]]"
date: 2024-09-27
topic: Demokratieprinzip
page_bfv: 643
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Stephan Brandner]] vom 27.9.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Der nächste #Thüringenputsch nach #Merkel! Diesmal auch noch devot flankiert durch den Thüringer Verfassungsgerichtshof... Was ist nur in [Symbol Deutsche-Flagge] los? Demokratie, Gewaltenteilung, Parlamentarismus werden durch die #Altparteien vernichtet! Täglich!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 643

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