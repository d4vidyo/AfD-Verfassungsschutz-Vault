---
type: zitat
speaker: "[[Martin Renner]]"
date: 2022-05-14
topic: Demokratieprinzip
page_bfv: 599
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 14.5.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>In der Tat macht es in der politischen Praxis keinen nennenswerten Unterschied mehr, bei welcher der genannten NED-Teilparteien man sein Kreuz macht. Im Ergebnis arbeiten sie alle gemeinsam an der zunehmenden Unfreiheit und der kommenden Verarmung des Wählers und Bürgers. [...] Herrschaftsfreier Diskurs - auch so eine schöne Worthülse unseres 'Jahrtausend-Dampfdenkers' Habermas. Der aber in Wirklichkeit nie etwas anderes meinte und anstrebte, als 'diskursfreie Herrschaft'. Und genau dafür haben sich die Medien à la 'Rheinische Post' zur Kampfmaschine der europaweit grassierenden Korporatokratie transformiert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 599

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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