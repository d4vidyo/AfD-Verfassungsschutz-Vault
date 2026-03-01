---
type: zitat
speaker: "[[Siegbert Droese]]"
date: 2023-09-03
topic: Demokratieprinzip
page_bfv: 586
source: 'None'
status: Unbewertet
---

# Zitat: [[Siegbert Droese]] vom 3.9.2023 veröffentlicht auf: 'None'
> [!quote] Aussage
>Und zur freundlichen Erinnerung, die hässliche Fratze des Faschismus unserer Tage.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 586

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