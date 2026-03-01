---
type: zitat
speaker: "[[Nicolaus Fest]]"
date: 2022-11-25
topic: Menschenwürde
page_bfv: 479
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Nicolaus Fest]] vom 25.11.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wenn man beispielsweise der Ansicht ist, dass die Muslime in Europa diskriminiert werden, macht man was? Genau! Man fragt Muslime, ob sie sich irgendwie diskriminiert fühlen, wenn sie keine Burkas in Schulen und keine Macheten und Sprengstoffgürtel im öffentlichen Raum tragen dürfen.

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