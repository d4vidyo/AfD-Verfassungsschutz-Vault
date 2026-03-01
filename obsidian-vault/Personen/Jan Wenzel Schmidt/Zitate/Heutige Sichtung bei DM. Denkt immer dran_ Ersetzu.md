---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2024-02-12
topic: Menschenwürde
page_bfv: 469
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 12.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Heutige Sichtung bei DM. Denkt immer dran: Ersetzungsmigration und Islamisierung sind nur rechte Verschwörungstheorien. Oder entsprechen sie vielleicht doch der Realität, weil jeder Bürger mit eigenen Augen in Echtzeit beobachten kann, wie sich diese bitterer Zustand im Alltag immer mehr bemerkbar macht?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 469

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