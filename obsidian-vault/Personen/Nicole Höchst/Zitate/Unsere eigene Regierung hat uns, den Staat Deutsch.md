---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2023-11-22
topic: Menschenwürde
page_bfv: 246
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 22.11.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Unsere eigene Regierung hat uns, den Staat Deutschland und seine Bürger, abgewirtschaftet und erhöht Tag für Tag unser Bürgerkriegs- und Armutsrisiko. Das Schlimmste in meinen Augen ist: Sie kommt damit durch.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 246

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