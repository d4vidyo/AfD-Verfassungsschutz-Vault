---
type: zitat
speaker: "[[Enxhi Seli-Zacharias]]"
date: 2022-05-19
topic: Menschenwürde
page_bfv: 461
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Enxhi Seli-Zacharias]] vom 19.5.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>\<Bild Mein Vater sagt, der Klimawandel wird weiter fortschreiten. Mein Vater sagt, die Pandemie wird uns noch lange beschäftigen. Mein Vater sagt, dass das bald eue geringsten Probleme sein werden.\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 461

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