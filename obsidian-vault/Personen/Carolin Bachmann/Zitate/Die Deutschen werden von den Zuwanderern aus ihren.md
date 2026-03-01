---
type: zitat
speaker: "[[Carolin Bachmann]]"
date: 2022-10-08
topic: Menschenwürde
page_bfv: 178
source: 'www.compact-online.de'
status: Unbewertet
---

# Zitat: [[Carolin Bachmann]] vom 8.10.2022 veröffentlicht auf: 'www.compact-online.de'
> [!quote] Aussage
>Die Deutschen werden von den Zuwanderern aus ihren Städten regelrecht herausgedrückt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 178

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