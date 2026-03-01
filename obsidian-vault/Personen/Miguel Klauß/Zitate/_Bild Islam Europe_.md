---
type: zitat
speaker: "[[Miguel Klauß]]"
date: 2023-11-04
topic: Menschenwürde
page_bfv: 476
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Miguel Klauß]] vom 4.11.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>\<Bild Islam Europe\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 476

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