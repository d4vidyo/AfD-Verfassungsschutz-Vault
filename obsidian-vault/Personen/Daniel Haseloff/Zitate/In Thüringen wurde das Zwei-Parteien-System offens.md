---
type: zitat
speaker: "[[Daniel Haseloff]]"
date: 2024-09-29
topic: Demokratieprinzip
page_bfv: 568
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Daniel Haseloff]] vom 29.9.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>In Thüringen wurde das Zwei-Parteien-System offensichtlich. Es gibt nur noch den Kartellblock und die #AfD. Die etablierten Parteien konnten sich damit auf Landesebene noch etwas Zeit verschaffen. Die erste Quittung kommt zur Bundestagswahl.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 568

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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