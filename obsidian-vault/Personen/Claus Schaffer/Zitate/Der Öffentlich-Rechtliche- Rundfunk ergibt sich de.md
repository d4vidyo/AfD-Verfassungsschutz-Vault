---
type: zitat
speaker: "[[Claus Schaffer]]"
date: 2022-08-26
topic: Demokratieprinzip
page_bfv: 560
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Claus Schaffer]] vom 26.8.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der Öffentlich-Rechtliche- Rundfunk ergibt sich dem Trend der 'Bücherverbrennung 2.0'.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 560

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