---
type: zitat
speaker: "[[Norbert Mayer]]"
date: 2023-10-30
topic: Demokratieprinzip
page_bfv: 632
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Norbert Mayer]] vom 30.10.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ein vom Volk frisch gewählter Landtagsabgeordneter wird von der Justiz direkt vor der konstituierenden Sitzung des Parlaments von Bayern abgefangen und in Haft genommen. CDU/CSU, in welche Bananenrepublik habt Ihr unser geliebtes Deutschland verschandelt?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 632

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