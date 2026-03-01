---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2024-07-08
topic: Menschenwürde
page_bfv: 372
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 8.7.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Was ist das schon wieder für eine komplett geisteskranke, antideutsche & geschichtsvergessene Aussage @welt? Sollen hier die heimatvertriebenen Deutschen etwa mit der illegalen Millionenarmee der orientalischen Glücksritter gleichgesetzt werden? Ekelhaft. Sie verachten unser Volk!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 372

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