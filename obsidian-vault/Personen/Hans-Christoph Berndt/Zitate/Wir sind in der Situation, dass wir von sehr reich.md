---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2022-10-31
topic: Menschenwürde
page_bfv: 230
source: 'Interview, veröffentlicht auf AIF1.tv'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 31.10.2022 veröffentlicht auf: 'Interview, veröffentlicht auf AIF1.tv'
> [!quote] Aussage
>Wir sind in der Situation, dass wir von sehr reichen und sehr einflussreichen und mächtigen Leuten, dass sehr einflussreiche und mächtige Leute die Transformation wollen, dass wir nicht mehr so leben, wie wir es gewohnt sind, nicht mehr in Nationalstaaten leben, nicht mehr frei leben, sondern in einer, ich würde mal sagen maoistischen Weltkommune leben, so, wie die es für richtig halten. Das ist die Lage, und dagegen muss man sich wehren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 230

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