---
type: zitat
speaker: "[[René Bochmann]]"
date: 2023-06-01
topic: Menschenwürde
page_bfv: 413
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[René Bochmann]] vom 1.6.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Unser Parteivorsitzender Tino Chrupalla verlangt zurecht dass das Asylrecht zur Disposition gestellt werden muss, wenn es nicht im deutschen Interesse funktioniert. Eine Remigrationsoffensive ist unseres Erachtens darüber hinaus nötig!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 413

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