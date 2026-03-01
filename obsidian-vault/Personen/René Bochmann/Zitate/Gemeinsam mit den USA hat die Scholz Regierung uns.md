---
type: zitat
speaker: "[[René Bochmann]]"
date: 2023-10-01
topic: Demokratieprinzip
page_bfv: 550
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[René Bochmann]] vom 1.10.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Gemeinsam mit den USA hat die Scholz Regierung unser Land angegriffen. [...] Sie haben uns verraten und bewusst und gewollt unser Land wirtschaftlich ruiniert. Und sie lachen uns dabei aus [...] Und sie stürzen uns durch Waffenlieferungen in einen Krieg gegen Russland.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 550

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