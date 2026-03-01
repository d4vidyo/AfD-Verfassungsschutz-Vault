---
type: zitat
speaker: "[[Peter Boehringer]]"
date: 2021-11-15
topic: Demokratieprinzip
page_bfv: 613
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Peter Boehringer]] vom 15.11.2021 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Die juristische Begründung des Zivilisationsbruchs tja... letzten Endes wird hier mit Macht... man macht es, wenn man es kann und wenn man es will. Warum auch immer. [...] Das ist alles völlig totalitär, muss man inzwischen sagen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 613

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