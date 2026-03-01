---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2022-10-15
topic: Sonstiges
page_bfv: 826
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 15.10.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Jugendorganisation und Mutterpartei werden zum Wohl unseres Landes Hand in Hand gehen. Auf gute Zusammenarbeit!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 826

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