---
type: zitat
speaker: "[[Wolfgang von Eyb]]"
date: 2022-04-07
topic: Demokratieprinzip
page_bfv: 620
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Wolfgang von Eyb]] vom 7.4.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wir müssen dran bleiben, damit sich die Befürworter der "Impfung" nicht neu gruppieren. Gewonnen ist die Sache erst, wenn der Nürnberger Prozess 2.0 eröffnet wird.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 620

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