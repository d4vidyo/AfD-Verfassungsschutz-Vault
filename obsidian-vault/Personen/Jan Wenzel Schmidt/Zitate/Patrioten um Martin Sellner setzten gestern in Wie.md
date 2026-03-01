---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2023-04-17
topic: Sonstiges
page_bfv: 782
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 17.4.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Patrioten um Martin Sellner setzten gestern in Wien ein starkes Zeichen gegen Frühsexualisierungsshows von Transen vor kleinen Kindern. Vor dem 'Schwulenhaus', wo die Indoktrination stattfand, fanden sich mutige Patrioten ein, um gegen den Wahnsinn zu demonstrieren. Die Woke-Ideologie greift nach unseren Kindern. Wer hier noch schweigt, stimmt zu.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 782

**Verfassungsschutz Kategorisierung:** Sonstiges.

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