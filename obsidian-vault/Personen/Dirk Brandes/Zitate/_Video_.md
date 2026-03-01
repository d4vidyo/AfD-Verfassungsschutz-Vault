---
type: zitat
speaker: "[[Dirk Brandes]]"
date: 2024-08-05
topic: Menschenwürde
page_bfv: 314
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Dirk Brandes]] vom 5.8.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>\<Video\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 314

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