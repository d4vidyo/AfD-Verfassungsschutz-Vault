---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2023-08-16
topic: Menschenwürde
page_bfv: 211
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 16.8.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Woher kommen denn auf einmal diese ganzen Familien? An einer hohen Geburtenrate kann es jedenfalls nicht liegen. Die ist in Deutschland nach wie vor sehr niedrig. Warum gibt es also Platzmangel? Liegt es vielleicht an der Ersetzungsmigration?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 211

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