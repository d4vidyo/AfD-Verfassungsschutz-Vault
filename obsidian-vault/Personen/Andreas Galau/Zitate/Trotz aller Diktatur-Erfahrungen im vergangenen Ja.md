---
type: zitat
speaker: "[[Andreas Galau]]"
date: 2021-09-07
topic: Demokratieprinzip
page_bfv: 619
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Andreas Galau]] vom 7.9.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Trotz aller Diktatur-Erfahrungen im vergangenen Jahrhundert ignoriert man die damaligen verbrecherischen medizinischen Experimente an Menschen und spuckt auf den daraus entstandenen "Nürnberger Kodex".

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 619

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