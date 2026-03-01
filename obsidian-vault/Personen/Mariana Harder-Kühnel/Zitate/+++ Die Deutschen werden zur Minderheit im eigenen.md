---
type: zitat
speaker: "[[Mariana Harder-Kühnel]]"
date: 2021-04-23
topic: Menschenwürde
page_bfv: 238
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Mariana Harder-Kühnel]] vom 23.4.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>+++ Die Deutschen werden zur Minderheit im eigenen Land! +++ Das ist keine Verschwörungstheorie, sondern simple Mathematik. Und es hängt mit der demografischen Katastrophe zusammen, in der sich unser Land seit Jahrzehnten befindet.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 238

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