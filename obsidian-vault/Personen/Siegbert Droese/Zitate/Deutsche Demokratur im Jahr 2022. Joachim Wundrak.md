---
type: zitat
speaker: "[[Siegbert Droese]]"
date: 2022-03-24
topic: Demokratieprinzip
page_bfv: 608
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Siegbert Droese]] vom 24.3.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Deutsche Demokratur im Jahr 2022. Joachim Wundrak und André Hahn scheitern: Gremium zur Geheimdienstkontrolle gewählt - AfD und Linke nicht dabei

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 608

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