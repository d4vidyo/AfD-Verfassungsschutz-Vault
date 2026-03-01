---
type: zitat
speaker: "[[Beatrix von Storch]]"
date: 2024-01-12
topic: Menschenwürde
page_bfv: 513
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Beatrix von Storch]] vom 12.1.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>#Deportation trendet um AfD-Verbot zu begründen: #Correctiv ist das Sturmgeschütz der grünen Milliardäre u. d. globalen Finanzindustrie.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 513

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