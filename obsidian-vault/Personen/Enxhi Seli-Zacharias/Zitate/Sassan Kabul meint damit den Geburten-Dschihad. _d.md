---
type: zitat
speaker: "[[Enxhi Seli-Zacharias]]"
date: 2025-01-20
topic: Menschenwürde
page_bfv: 936
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Enxhi Seli-Zacharias]] vom 20.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Sassan Kabul meint damit den Geburten-Dschihad. #dschihad

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 936

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