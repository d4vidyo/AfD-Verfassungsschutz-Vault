---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2023-03-16
topic: Menschenwürde
page_bfv: 346
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 16.3.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Fachkräfte kommen nicht mit dem Schlauchboot, zerlegen keine Innenstädte, vergewaltigen keine Frauen und kassieren kein Bürgergeld. Echte Fachkräfte verlassen Deutschland jedes Jahr. Zu Tausenden!

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