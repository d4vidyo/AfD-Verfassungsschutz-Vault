---
type: zitat
speaker: "[[René Springer]]"
date: 2025-01-26
topic: Menschenwürde
page_bfv: 888
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 26.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die Grünen hingegen wollen an der totalen Zerstörung Deutschlands durch Massenmigration festhalten. Spätestens heute weiß jeder, für welchen Wahnsinn diese Partei steht!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 888

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