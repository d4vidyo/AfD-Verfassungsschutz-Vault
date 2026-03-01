---
type: zitat
speaker: "[[Thorsten Weiß]]"
date: 2024-10-01
topic: Menschenwürde
page_bfv: 351
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Thorsten Weiß]] vom 1.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die #Migrantenquote soll Status als multikulturelle Gesellschaft zementieren. Dass diese auch immer multikriminell ist, wird in Kauf genommen. Messerterror, Vergewaltigungen. Belästigungen, explodierende Kriminalität sind akzeptable Begleiterscheinungen. Deshalb nur noch #AfD!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 351

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