---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2021-06-29
topic: Demokratieprinzip
page_bfv: 578
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom 29.6.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>In beiden deutschen Diktaturen forderten die politischen Machthaber diese Art von Untergebenheit. Geschichte wiederholt sich

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 578

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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