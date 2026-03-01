---
type: zitat
speaker: "[[Daniel Haseloff]]"
date: 2024-06-01
topic: Sonstiges
page_bfv: 707
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Daniel Haseloff]] vom 1.6.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Das ist die richtige Frage.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 707

**Verfassungsschutz Kategorisierung:** Sonstiges.

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