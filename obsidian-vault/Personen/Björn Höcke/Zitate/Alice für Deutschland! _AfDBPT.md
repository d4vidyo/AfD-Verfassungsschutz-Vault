---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2025-01-11
topic: Nationalsozialismus
page_bfv: 983
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 11.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Alice für Deutschland! #AfDBPT

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 983

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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