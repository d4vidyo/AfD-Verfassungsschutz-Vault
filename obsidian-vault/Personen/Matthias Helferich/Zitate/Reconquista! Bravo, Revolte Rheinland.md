---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-03-27
topic: Sonstiges
page_bfv: 778
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 27.3.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Reconquista! Bravo, Revolte Rheinland

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 778

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