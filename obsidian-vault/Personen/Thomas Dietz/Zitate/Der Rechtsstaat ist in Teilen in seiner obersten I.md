---
type: zitat
speaker: "[[Thomas Dietz]]"
date: 2022-05-19
topic: Demokratieprinzip
page_bfv: 625
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Thomas Dietz]] vom 19.5.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der Rechtsstaat ist in Teilen in seiner obersten INSTANZ nicht mehr existent. Das ist politisch gewollte Rechtsprechung!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 625

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