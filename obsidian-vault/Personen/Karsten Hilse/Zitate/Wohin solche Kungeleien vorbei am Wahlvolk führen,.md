---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2022-03-01
topic: Demokratieprinzip
page_bfv: 627
source: 'Blaue Post Bautzen'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom März 2022 veröffentlicht auf: 'Blaue Post Bautzen'
> [!quote] Aussage
>Wohin solche Kungeleien vorbei am Wahlvolk führen, zeigen Totalausfälle wie Wulff oder Steinmeier, die das Amt als politische Sprechpuppen immer mehr beschädigen.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: März 2022

**SPIEGEL-Notiz:** Gutachten Seite: 627

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