---
type: zitat
speaker: "[[Franz Schmid]]"
date: 2025-01-07
topic: Menschenwürde
page_bfv: 885
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Franz Schmid]] vom 7.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Thema Vornamen in Berlin. Silvester 2040 kann heiter werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 885

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