---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2023-12-04
topic: Demokratieprinzip
page_bfv: 572
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 4.12.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wer nicht zum Kartell gehört, soll verboten werden - namens der Demokratie. [...] Was für eine Verkommenheit!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 572

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