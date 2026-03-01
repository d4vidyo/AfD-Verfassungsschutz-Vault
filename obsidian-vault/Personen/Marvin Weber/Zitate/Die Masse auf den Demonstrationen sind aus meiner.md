---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2024-02-03
topic: Demokratieprinzip
page_bfv: 574
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 3.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Masse auf den Demonstrationen sind aus meiner Sicht der letzte Hilfeschrei eines politmedialen Kartells, das die Sorgen und Nöte der deutschen Bürger, beispielsweise das Aufbegehren der Landwirte in Form der Bauernproteste, zu unterdrücken und zu verschleiern versucht. Es wirkt wie die inszenierten Proteste der Nachfolgepartei der SED, nämlich der PDS aus dem Jahre 1990, als inszenterte Großproteste zum 'Kampf gegen den Faschismus' und gegen 'Rechts' als letztes Aufbegehren eines entmachteten Unrechtsherrschaft inszeniert wurden. Die DDR-Staatsdoktrin lässt also grüßen im bunten Deutschland.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 574

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