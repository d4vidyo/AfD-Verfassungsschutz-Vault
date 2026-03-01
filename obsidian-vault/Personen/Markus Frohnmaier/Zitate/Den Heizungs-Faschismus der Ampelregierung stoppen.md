---
type: zitat
speaker: "[[Markus Frohnmaier]]"
date: 2023-09-08
topic: Demokratieprinzip
page_bfv: 649
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Markus Frohnmaier]] vom 8.9.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Den Heizungs-Faschismus der Ampelregierung stoppen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 649

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