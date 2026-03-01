---
type: zitat
speaker: "[[Thorsten Weiß]]"
date: 2022-11-23
topic: Demokratieprinzip
page_bfv: 578
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Thorsten Weiß]] vom 23.11.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Nach 80 Jahren tragen deutsche Minister im Ausland wieder Armbinde. #OneLove #Faeser

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