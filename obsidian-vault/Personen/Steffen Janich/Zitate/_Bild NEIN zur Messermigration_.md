---
type: zitat
speaker: "[[Steffen Janich]]"
date: 2023-01-26
topic: Menschenwürde
page_bfv: 299
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Steffen Janich]] vom 26.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>\<Bild NEIN zur Messermigration\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 299

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