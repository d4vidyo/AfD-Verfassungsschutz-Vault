---
type: zitat
speaker: "[[Gunnar Beck]]"
date: 2023-11-23
topic: Demokratieprinzip
page_bfv: 569
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Gunnar Beck]] vom 23.11.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die #BRD ist nach fast 75 Jahren ein Staat, den sich die #Kartellparteien zur Beute gemacht haben. Wir brauchen #Volksentscheide, auch über den Entzug der Alterssicherung für Politiker, die das Land zugrunde richten. #FailedStateGermany

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 569

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