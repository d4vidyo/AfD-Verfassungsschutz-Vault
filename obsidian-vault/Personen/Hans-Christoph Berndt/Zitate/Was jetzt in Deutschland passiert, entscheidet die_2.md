---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-12-31
topic: Nationalsozialismus
page_bfv: 980
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 31.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Was jetzt in Deutschland passiert, entscheidet die Zukunft Europas. Wenn die Deutschen endlich ihren Weltkriegs-Schuldkomplex loswerden, war es das für die Globalisten. Deutschland ist/war ihre wichtigste Bastion. Deshalb drehen sie so durch, wenn Musk die @AfD unterstützt.'

**Parser-Notiz:** Es handelt sich möglicherweise um ein Duplikat von dem Zitat: [[Was jetzt in Deutschland passiert, entscheidet die]]

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