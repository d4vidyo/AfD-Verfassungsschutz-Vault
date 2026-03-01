---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2025-01-15
topic: Demokratieprinzip
page_bfv: 966
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 15.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Eine Unvereinbarkeitsliste auf der obskure Kleinstorganisationen, nicht aber verbrecherische Massenorganisationen wie die Altparteien stehen, obwohl letzte Deutschland so schweren Schaden zugefügt haben, wie niemand sonst, ist letztlich halt auch nur ein absurder Witz.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 966

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