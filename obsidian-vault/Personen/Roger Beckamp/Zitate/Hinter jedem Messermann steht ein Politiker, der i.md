---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2022-08-15
topic: Menschenwürde
page_bfv: 303
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 15.8.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Hinter jedem Messermann steht ein Politiker, der ihn eingeladen hat. In jedem normalen Rechtsstaat würde es Unterstützung und Dankbarkeit für den Polizisten geben, der den Messer-Senegalesen gestoppt und damit Dortmund geschützt hat. In der heutigen Bundesrepublik läuft das natürlich anders

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 303

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