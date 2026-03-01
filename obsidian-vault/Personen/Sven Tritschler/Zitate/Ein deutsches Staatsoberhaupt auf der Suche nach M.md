---
type: zitat
speaker: "[[Sven Tritschler]]"
date: 2021-11-13
topic: Demokratieprinzip
page_bfv: 615
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Sven Tritschler]] vom 13.11.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ein deutsches Staatsoberhaupt auf der Suche nach Minderheiten, die als Sündenbock für die Versagerpolitik herhalten müssen. Bewährtes Konzept, allerdings seit rund 75 Jahren aus der Mode.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 615

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