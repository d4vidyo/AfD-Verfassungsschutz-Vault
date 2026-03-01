---
type: zitat
speaker: "[[Erika Steinbach]]"
date: 2022-08-12
topic: Demokratieprinzip
page_bfv: 571
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Erika Steinbach]] vom 12.8.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Unsere Demokratie verkommt unter Beteiligung des Parteienkartells von CDU/CSU, SPD, Grünen, FDP und Linkspartei zusehends in atemberaubender Geschwindigkeit.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 571

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