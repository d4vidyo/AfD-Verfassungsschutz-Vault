---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2024-07-21
topic: Sonstiges
page_bfv: 781
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 21.7.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Gut, dass es eine Jugend gibt, die sich laut, aber friedlich gegen die Verdrängung wehrt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 781

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