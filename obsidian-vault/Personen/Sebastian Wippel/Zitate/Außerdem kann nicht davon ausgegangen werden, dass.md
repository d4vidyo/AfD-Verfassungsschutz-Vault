---
type: zitat
speaker: "[[Sebastian Wippel]]"
date: 2023-06-08
topic: Menschenwürde
page_bfv: 206
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Sebastian Wippel]] vom 8.6.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Außerdem kann nicht davon ausgegangen werden, dass die Väter unseres Grundgesetzes bei der Verschriftlichung des Asylrechts für politisch Verfolgte vor mehr als 70 Jahren wohl kaum den demografischen Austausch des eigenen Volkes durch beruflich unqualifizierte und kulturfremde Migranten im Hinterkopf hatten.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 206

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