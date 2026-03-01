---
type: zitat
speaker: "[[Petr Bystron]]"
date: 2023-04-27
topic: Sonstiges
page_bfv: 744
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Petr Bystron]] vom 27.4.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der Systemschutz versucht, den Höhenflug der AfD zu stoppen. Die 'Junge Alternative' ist nicht rechtsextrem, genauso der Verein 'Ein Prozent' Beide leisten wichtige Arbeit zum Erhalt unserer Heimat.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 744

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