---
type: zitat
speaker: "[[Anna Leisten]]"
date: 2023-07-08
topic: Menschenwürde
page_bfv: 417
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Anna Leisten]] vom 8.7.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Soll die @JA_Deutschland auch eine Remigrationstour durch die Bundesrepublik planen? Remigrationsbus mit z.B. @Hannes_Gnauck und @TomaszFroelich am Steuer... Was meint ihr? Vielleicht noch diesen Sommer? Schreibt es in die Kommentare.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 417

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