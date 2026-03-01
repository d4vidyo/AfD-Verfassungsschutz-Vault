---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2022-03-23
topic: Demokratieprinzip
page_bfv: 623
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 23.3.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Corona ist nichts weiter als eine [...] fortgeschrittene Übung in den Totalitarismus des 21. Jahrhunderts und eine, die in Deutschland wiedereinmal mit besonderer Verbiesterung durchexerziert wird.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 623

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