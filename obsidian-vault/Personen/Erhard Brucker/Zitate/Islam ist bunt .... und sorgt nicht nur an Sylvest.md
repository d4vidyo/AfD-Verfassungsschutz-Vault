---
type: zitat
speaker: "[[Erhard Brucker]]"
date: 2022-10-31
topic: Menschenwürde
page_bfv: 479
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Erhard Brucker]] vom 31.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Islam ist bunt .... und sorgt nicht nur an Sylvester für einen Bombenstimmung… \<Bild When she's a 10, 9, 8, 7, 6..\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 479

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