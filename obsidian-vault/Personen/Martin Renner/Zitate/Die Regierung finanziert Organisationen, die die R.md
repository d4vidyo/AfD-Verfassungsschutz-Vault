---
type: zitat
speaker: "[[Martin Renner]]"
date: 2024-02-05
topic: Demokratieprinzip
page_bfv: 598
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 5.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Regierung finanziert Organisationen, die die Regierungskritiker vertreiben sollen. Sozialistische Demokratie. DDR 2.0

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 598

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