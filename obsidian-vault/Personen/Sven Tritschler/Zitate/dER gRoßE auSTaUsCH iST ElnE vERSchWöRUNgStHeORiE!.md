---
type: zitat
speaker: "[[Sven Tritschler]]"
date: 2024-11-14
topic: Menschenwürde
page_bfv: 889
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Sven Tritschler]] vom 14.11.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>dER gRoßE auSTaUsCH iST ElnE vERSchWöRUNgStHeORiE!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 889

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