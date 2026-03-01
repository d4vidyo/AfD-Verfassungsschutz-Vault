---
type: zitat
speaker: "[[Martin Renner]]"
date: 2024-02-17
topic: Demokratieprinzip
page_bfv: 584
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 17.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Denkst Du oppositionell, dann wirst Du ausspioniert. Von Bürokraten, die das Werkzeug der Diktatoren sind.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 584

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