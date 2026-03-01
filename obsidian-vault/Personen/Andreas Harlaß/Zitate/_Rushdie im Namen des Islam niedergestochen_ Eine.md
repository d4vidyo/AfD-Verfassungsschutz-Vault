---
type: zitat
speaker: "[[Andreas Harlaß]]"
date: 2022-08-13
topic: Menschenwürde
page_bfv: 480
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Andreas Harlaß]] vom 13.8.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>#Rushdie im Namen des Islam niedergestochen? Eine Religion, die so martialisch gegen Andersdenkende vorgeht, sollte als terroristische Vereinigung in der freien Welt eingestuft werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 480

**Verfassungsschutz Kategorisierung:** Verstoß gegen die Menschenwürde.

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