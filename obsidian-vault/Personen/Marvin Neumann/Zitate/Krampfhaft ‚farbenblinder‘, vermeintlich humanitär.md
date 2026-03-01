---
type: zitat
speaker: "[[Marvin Neumann]]"
date: 2022-03-16
topic: Menschenwürde
page_bfv: 334
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Marvin Neumann]] vom 16.3.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Krampfhaft ‚farbenblinder‘, vermeintlich humanitärer Liberalismus tötet.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 334

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