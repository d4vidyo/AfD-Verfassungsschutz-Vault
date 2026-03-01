---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2023-03-01
topic: Sonstiges
page_bfv: 781
source: 'Blaue Zukunft'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom März 2023 veröffentlicht auf: 'Blaue Zukunft'
> [!quote] Aussage
>Aus diesem Grund unterstütze ich seit Jahren die identitäre Bewegung (IB) bei ihrer wichtigen Arbeit.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: März 2023

**SPIEGEL-Notiz:** Gutachten Seite: 781

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