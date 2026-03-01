---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-05-30
topic: Sonstiges
page_bfv: 761
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 30.5.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Kaiser ist einer der klügsten Köpfe des publizistischen Vorfelds. Die #AfD wäre dumm, wenn sie sich von ihm lösen würde, nur um der WELT zu gefallen. #solidaritaetisteinewaffe

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 761

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