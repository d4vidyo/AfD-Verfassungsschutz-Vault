---
type: zitat
speaker: "[[Hannes Gnauck]]"
date: 2021-11-04
topic: Sonstiges
page_bfv: 723
source: 'RBB24'
status: Unbewertet
---

# Zitat: [[Hannes Gnauck]] vom 4.11.2021 veröffentlicht auf: 'RBB24'
> [!quote] Aussage
>Unterstützungswerten Projekten, die sich für den Erhalt unserer Heimat einsetzen, werde ich immer unter die Arme greifen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 723

**Verfassungsschutz Kategorisierung:** Sonstiges.

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