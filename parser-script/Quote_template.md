---
type: zitat
speaker: "[[>>speaker<<]]"
date: >>date_normalized<<
topic: >>main_topic<<
page_bfv: >>page<<
source: >>source<<
status: Unbewertet
---

# Zitat: [[>>speaker<<]] vom >>date<< veröffentlicht auf: >>source<<
> [!quote] Aussage
>>>quote<<

**Parser-Notiz:** >>parse_note<<

**SPIEGEL-Notiz:** >>note<<

**Verfassungsschutz Kategorisierung:** >>topic_long<<

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