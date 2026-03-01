---
type: zitat
speaker: "[[Harald Laatsch]]"
date: 2023-12-31
topic: Demokratieprinzip
page_bfv: 630
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Harald Laatsch]] vom 31.12.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Zusammen mit Gewerkschaften, Kirchen, Medien, Parteien, WEF usw. bilden die Verbände den tiefen Staat, die größte Gefahr für die Demokratie.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 630

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