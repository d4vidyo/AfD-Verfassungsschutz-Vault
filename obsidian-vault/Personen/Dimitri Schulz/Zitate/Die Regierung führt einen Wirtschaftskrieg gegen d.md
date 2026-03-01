---
type: zitat
speaker: "[[Dimitri Schulz]]"
date: 2022-09-06
topic: Demokratieprinzip
page_bfv: 648
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Dimitri Schulz]] vom 6.9.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Regierung führt einen Wirtschaftskrieg gegen das deutsche Volk

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 648

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