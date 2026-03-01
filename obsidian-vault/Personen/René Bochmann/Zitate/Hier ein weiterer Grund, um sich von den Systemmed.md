---
type: zitat
speaker: "[[René Bochmann]]"
date: 2023-11-11
topic: Demokratieprinzip
page_bfv: 559
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[René Bochmann]] vom 11.11.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Hier ein weiterer Grund, um sich von den Systemmedien abzuwenden, hin zur Realität. Deshalb Deutschland Kurier statt Spiegel!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 559

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