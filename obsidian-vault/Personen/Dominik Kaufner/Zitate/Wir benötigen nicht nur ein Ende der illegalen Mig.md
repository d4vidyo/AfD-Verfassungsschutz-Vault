---
type: zitat
speaker: "[[Dominik Kaufner]]"
date: 2024-12-14
topic: Menschenwürde
page_bfv: 929
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Dominik Kaufner]] vom 14.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wir benötigen nicht nur ein Ende der illegalen Migration, sondern vor allem eine großangelegte #Remigration. Millionenfach.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 929

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