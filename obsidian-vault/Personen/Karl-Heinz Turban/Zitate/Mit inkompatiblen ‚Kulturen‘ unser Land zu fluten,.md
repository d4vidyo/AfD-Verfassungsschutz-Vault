---
type: zitat
speaker: "[[Karl-Heinz Turban]]"
date: 2022-10-19
topic: Menschenwürde
page_bfv: 340
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Karl-Heinz Turban]] vom 19.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Mit inkompatiblen ‚Kulturen‘ unser Land zu fluten, endet tödlich...

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 340

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