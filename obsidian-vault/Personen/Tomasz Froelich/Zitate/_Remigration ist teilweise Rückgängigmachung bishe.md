---
type: zitat
speaker: "[[Tomasz Froelich]]"
date: 2024-01-11
topic: Menschenwürde
page_bfv: 138
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Tomasz Froelich]] vom 11.1.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>#Remigration ist teilweise Rückgängigmachung bisher stattgefundener Migration. Fordert die AfD seit Jahren. Und mittlerweile selbst Scholz. Illegale nicht abzuschieben ist ein Skandal, nicht umgekehrt! Und Ausbürgerung zB von Kriminellen zu prüfen, sollte selbstverständlich sein.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 138

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