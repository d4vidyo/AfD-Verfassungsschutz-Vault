---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2024-09-23
topic: Menschenwürde
page_bfv: 411
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 23.9.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wir leben halt unsere Überzeugungen! #abschieben

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 411. Tweet mit einem Screenshot eines Welt-Artikels "AfD-Anhänger grölen Song auf Wahlparty - 'Wir schieben sie alle ab'"

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