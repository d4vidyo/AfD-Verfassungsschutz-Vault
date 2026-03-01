---
type: zitat
speaker: "[[Franz Schmid]]"
date: 2023-07-12
topic: Sonstiges
page_bfv: 789
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Franz Schmid]] vom 12.7.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ich verstehe dieses Verhalten nicht? Was erwarten unsere Freunde aus Oberösterreich, wenn sie einem Aktionsplan gegen Extremismus aka Repression gegen unser friedliches, patriotisches Vorfeld zustimmen? Applaus vom Gegner? Akzeptanz in hohen Kreisen? Das wird nicht passieren!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 789

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