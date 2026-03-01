---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2024-07-08
topic: Menschenwürde
page_bfv: 346
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 8.7.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wie wäre es mit Waggons nur für Deutsche? Das würde das Problem ebenfalls effektiv lösen und würde darüber hinaus nicht nur die Frauen, sondern auch deutsche Männer schützen. #RemigrationJetzt #FestungEuropa

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 346

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