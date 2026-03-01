---
type: zitat
speaker: "[[Oliver Kirchner]]"
date: 2023-02-24
topic: Menschenwürde
page_bfv: 346
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Oliver Kirchner]] vom 24.2.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>#Fachkräfte kommen nicht mit dem Schlauchboot über das Mittelmeer, sie zerlegen keine Innenstädte, sie vergewaltigen keine Frauen, sie kassieren kein Bürgergeld, sie stoßen keine Frauen und Kinder vor Züge, sie verüben keine Terroranschläge und sie stechen nicht wahllos auf ihre Aufnahmegesellschaft ein. Richtige Fachkräfte verlassen Deutschland, jeden Tag, jede Woche und jedes Jahr, und zwar deutsche Fachkräfte. Diese Entwicklung ist zu stoppen und zwar sofort. #AfD #AfDLSA #Asylmissbrauch.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 346

**Verfassungsschutz Kategorisierung:** Verstoß gegen die Menschenwürde.

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