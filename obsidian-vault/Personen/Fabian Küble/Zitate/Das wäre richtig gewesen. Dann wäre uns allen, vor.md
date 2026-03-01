---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2025-02-19
topic: Nationalsozialismus
page_bfv: 980
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 19.2.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Das wäre richtig gewesen. Dann wäre uns allen, vor allem Großbritannien selbst, viel erspart geblieben. Stattdessen gab es Weltkrieg. Offenbar wollen Leute wie sie das wieder. Sie sind gefährlich. Gut das Trump damit nun Schluss macht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 980

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