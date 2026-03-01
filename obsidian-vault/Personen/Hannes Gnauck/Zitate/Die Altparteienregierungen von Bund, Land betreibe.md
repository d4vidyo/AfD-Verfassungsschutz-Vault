---
type: zitat
speaker: "[[Hannes Gnauck]]"
date: 2023-04-17
topic: Menschenwürde
page_bfv: 195
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Hannes Gnauck]] vom 17.4.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die Altparteienregierungen von Bund, Land betreiben hier einen Bevölkerungsaustausch und sie werden nicht ruhen, bis jeder Winkel unseres Landes und jedes friedliche Dorf mit illegalen Migranten vollgestopft ist.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 195

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