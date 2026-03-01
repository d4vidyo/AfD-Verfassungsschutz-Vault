---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2024-03-04
topic: Sonstiges
page_bfv: 790
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 4.3.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Was soll an den 'Ideen eines Herrn Sellner' denn so schlimm sein?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 790

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