---
type: zitat
speaker: "[[Alexander Jungbluth]]"
date: 2024-04-29
topic: Menschenwürde
page_bfv: 462
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Alexander Jungbluth]] vom 29.4.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Islamisten bedrohen unsere Werte Ampel macht Deutschland zum Kalifat!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 462

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