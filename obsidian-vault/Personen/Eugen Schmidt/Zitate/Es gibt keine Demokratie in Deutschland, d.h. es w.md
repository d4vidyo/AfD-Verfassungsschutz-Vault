---
type: zitat
speaker: "[[Eugen Schmidt]]"
date: 2022-03-10
topic: Demokratieprinzip
page_bfv: 557
source: 'Videobeitrag'
status: Unbewertet
---

# Zitat: [[Eugen Schmidt]] vom 10.3.2022 veröffentlicht auf: 'Videobeitrag'
> [!quote] Aussage
>Es gibt keine Demokratie in Deutschland, d.h. es wird eine einheitliche Meinung aufgedrängt, und zwar von der regierenden Elite und alle anderen politischen Meinungen werden mit allen möglichen Mitteln unterdrückt: Im Internet, in den Medien, unter anderem auch durch körperliche Übergriffe auf Andersdenkende.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 557

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