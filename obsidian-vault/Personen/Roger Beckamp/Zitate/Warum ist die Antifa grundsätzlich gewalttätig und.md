---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2022-08-22
topic: Sonstiges
page_bfv: 777
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 22.8.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Warum ist die Antifa grundsätzlich gewalttätig und schlecht erzogen, vor allem im Gespräch? Warum ist die identitäre Bewegung stets friedlich, klettert auf Häuser und entrollt kreative Sprüche?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 777

**Verfassungsschutz Kategorisierung:** Sonstiges.

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