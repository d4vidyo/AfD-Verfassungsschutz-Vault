---
type: zitat
speaker: "[[Harald Laatsch]]"
date: 2022-12-11
topic: Demokratieprinzip
page_bfv: 634
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Harald Laatsch]] vom 11.12.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wir erleben einen Staatsstreich, aber nicht von #Reichsbürger Rentnern, sondern direkt aus dem Innenministerium, dort wo die staatliche Waffengewalt gebündelt ist. Das ist wahrhaft ein Grund Angst zu haben! #Faeser vernichtet die Demokratie.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 634

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