---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2024-02-13
topic: Sonstiges
page_bfv: 743
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 13.2.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ein starkes und wichtiges Zeichen zum Jahrestag der #Bombardierung Dresdens im Jahr1945. Es ist Zeit für ein würdiges Gedenken.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 743

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