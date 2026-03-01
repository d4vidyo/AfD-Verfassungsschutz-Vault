---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2023-01-03
topic: Menschenwürde
page_bfv: 354
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 3.1.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die linke Utopie des friedlichen Multikulturistan wurde schon 2015 in Köln vergewaltigt! In Berlin hat sie #Silvester2022 gebrannt! Immer waren die Haupttäter importierte Kriminelle!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 354

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