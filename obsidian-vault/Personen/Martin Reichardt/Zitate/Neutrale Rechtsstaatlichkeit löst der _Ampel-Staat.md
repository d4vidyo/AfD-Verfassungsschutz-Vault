---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2024-01-27
topic: Sonstiges
page_bfv: 785
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 27.1.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Neutrale Rechtsstaatlichkeit löst der #Ampel-Staat weiter auf! Gewaltverbrecher werden mit albernen Begründungen nicht ausgewiesen oder zu lächerlichen Strafen verurteilt. Wer aber linken Meinungstotalitaristen nicht passt, darf nicht einreisen! #Sellner

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 785

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