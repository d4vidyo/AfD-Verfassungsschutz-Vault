---
type: zitat
speaker: "[[Andreas Harlaß]]"
date: 2021-11-27
topic: Menschenwürde
page_bfv: 154
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Andreas Harlaß]] vom 27.11.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>TV-Werbung 2021: Haben wir unsere Kolonien wieder?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 154

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