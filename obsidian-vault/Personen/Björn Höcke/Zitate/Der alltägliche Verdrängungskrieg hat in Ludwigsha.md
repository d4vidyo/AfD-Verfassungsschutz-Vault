---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-10-22
topic: Menschenwürde
page_bfv: 477
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 22.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der alltägliche Verdrängungskrieg hat in Ludwigshafen-Oggersheim zwei weitere Opfer gefordert [...] Der Täter ist ein somalischer Asyl-Einwanderer [...]. Wahrscheinlich ist der Täter psychisch krank und leidet an jener unter Einwanderern weit verbreiteten Volkskrankheit, welche die Betroffenen ,Allahu Akbar' schreien lässt und deren Wahrnehmung so verzerrt, daß sie in den ,ungläubigen' Gastgebern lebensunwertes Leben sehen. Also nichts Besonderes.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 477

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