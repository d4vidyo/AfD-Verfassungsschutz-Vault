---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2022-10-20
topic: Menschenwürde
page_bfv: 291
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 20.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Beinahe täglich sind Opfer von migrantischen Metzeleien und (Massen-) Vergewaltigungen zu beklagen, während wir immer die gleiche Leier von eingebildetem Rassismus und Islamophobie hören.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 291

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