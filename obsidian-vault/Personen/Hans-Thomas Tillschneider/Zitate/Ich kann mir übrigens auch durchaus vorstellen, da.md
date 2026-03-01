---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2021-10-09
topic: Demokratieprinzip
page_bfv: 621
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 9.10.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ich kann mir übrigens auch durchaus vorstellen, dass hinter der Corona-Politik eine Elite steht, die eine neue Weltordnung schaffen will!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 621

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