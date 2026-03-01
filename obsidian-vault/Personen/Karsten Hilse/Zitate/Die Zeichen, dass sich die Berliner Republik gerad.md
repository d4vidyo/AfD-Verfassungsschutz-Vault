---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2021-08-04
topic: Demokratieprinzip
page_bfv: 578
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom 4.8.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Zeichen, dass sich die Berliner Republik gerade in Richtung Totalitarismus entwickelt, sind unübersehbar. Niemand wird sagen können: 'Ich habe nichts gewusst'.

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