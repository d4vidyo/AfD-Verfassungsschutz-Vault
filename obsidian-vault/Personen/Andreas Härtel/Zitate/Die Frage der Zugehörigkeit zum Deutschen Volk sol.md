---
type: zitat
speaker: "[[Andreas Härtel]]"
date: 2024-08-03
topic: Menschenwürde
page_bfv: 133
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Andreas Härtel]] vom 3.8.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Frage der Zugehörigkeit zum Deutschen Volk sollte künftig nicht nur eine formaljuristische Dimension haben, sondern in erster Linie eine ethnisch- kulturelle. Auch da bin ich ganz #AfD.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 133

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