---
type: zitat
speaker: "[[Andreas Harlaß]]"
date: 2021
topic: Menschenwürde
page_bfv: 228
source: 'None'
status: Unbewertet
---

# Zitat: [[Andreas Harlaß]] vom 2021 veröffentlicht auf: 'None'
> [!quote] Aussage
>Wir importieren frauenfeindliche, kindersexuellaffine und naturfeindliche Menscheit massenweise, füttern sie auf Kosten unserer Renter und fühlen uns als gute Menschen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 228

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