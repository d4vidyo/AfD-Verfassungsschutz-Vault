---
type: zitat
speaker: "[[Martin Renner]]"
date: 2024-06-04
topic: Menschenwürde
page_bfv: 481
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 4.6.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>,Friedlicher' Islam ist ein Märchen, so wie der bisher nur noch ,nicht richtig' durchgeführte Sozialismus.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 481

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