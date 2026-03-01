---
type: zitat
speaker: "[[Peter Felser]]"
date: 2022-07-22
topic: Menschenwürde
page_bfv: 228
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Peter Felser]] vom 22.7.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Deutschlands Bevölkerung wird transformiert. Ob absichtlich oder aus Naivität spielt hier keine Rolle. Die Migration ist und bleibt die existenzielle Gefahr für unser Land.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 228

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