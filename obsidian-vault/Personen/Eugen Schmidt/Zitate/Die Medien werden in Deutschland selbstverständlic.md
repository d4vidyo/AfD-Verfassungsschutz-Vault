---
type: zitat
speaker: "[[Eugen Schmidt]]"
date: 2022-03-10
topic: Demokratieprinzip
page_bfv: 558
source: 'Videobeitrag'
status: Unbewertet
---

# Zitat: [[Eugen Schmidt]] vom 10.3.2022 veröffentlicht auf: 'Videobeitrag'
> [!quote] Aussage
>Die Medien werden in Deutschland selbstverständlich komplett von der Regierung kontrolliert. Alternative, oppositionelle Meinungen sind nicht vertreten.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 558

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