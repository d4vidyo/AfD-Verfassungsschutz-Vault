---
type: zitat
speaker: "[[Reimond Hoffmann]]"
date: 2022-11-29
topic: Menschenwürde
page_bfv: 189
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Reimond Hoffmann]] vom 29.11.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die wollen sich innerhalb von drei Jahren neue Wähler einbürgern. Die etablierte Politik holt sich gezielt eine neue Wählerschaft ins Land und lässt sie noch in der selben Legislaturperiode wählen. Die Ersetzungsmigration schaltet den Turbo ein. Ein Albtraum.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 189

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