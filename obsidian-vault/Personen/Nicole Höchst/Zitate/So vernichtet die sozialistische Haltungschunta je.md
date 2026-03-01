---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2023-08-30
topic: Demokratieprinzip
page_bfv: 606
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 30.8.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>So vernichtet die sozialistische Haltungschunta jede Tag Deutschland ein kleines Bißchen mehr.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 606

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