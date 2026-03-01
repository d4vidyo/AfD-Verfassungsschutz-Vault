---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2022-12-09
topic: Menschenwürde
page_bfv: 323
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 9.12.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>DARUM sind die Altparteien der FEIND!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 323

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