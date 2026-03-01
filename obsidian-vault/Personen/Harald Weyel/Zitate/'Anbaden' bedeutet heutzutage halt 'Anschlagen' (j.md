---
type: zitat
speaker: "[[Harald Weyel]]"
date: 2023-06-06
topic: Menschenwürde
page_bfv: 325
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Harald Weyel]] vom 6.6.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>'Anbaden' bedeutet heutzutage halt 'Anschlagen' (jedenfalls in #EU-#BRDMigratopia)...;((

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 325

**Verfassungsschutz Kategorisierung:** Verstoß gegen die Menschenwürde.

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