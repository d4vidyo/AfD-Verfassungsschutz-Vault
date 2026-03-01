---
type: zitat
speaker: "[[Rainer Rothfuß]]"
date: 2023-01-10
topic: Demokratieprinzip
page_bfv: 621
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Rainer Rothfuß]] vom 10.1.2023 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Wir können diese Zahl nicht einfach so im Raum stehen lassen. Wir müssen die zur Verantwortung ziehen, die dazu geführt haben, dass die Menschen ins Unglück gestürzt wurden, dass die Abtreibungen in die Höhe schnellen, dass die psychischen Erkrankungen in die Höhe schnellen. Und da werden wir als AfD ein unangenehmer Begleiter weiterhin dieser Politik sein, die gegen den Menschen gerichtet ist. [...] Und viele Menschen sagen ja immer wieder: "Parteien können das Ganze eh nicht verändern. Wählen hilft eh nichts. Wenn Wahlen was verändern würden, wären sie längst verboten worden." Aber ich würde sagen: Nein, sie wären nicht verboten worden, sondern sie würden manipuliert werden. Dadurch, dass einfach Gehirnwäsche gemacht wird, dass die Medien den Menschen falsche Fakten einflößen oder falsche Meinungen einflößen, dass sie gewisse Probleme einfach weglassen, dass sie die Verursacher nicht benennen der Probleme. Das ist ein ganz, ganz wichtiger Faktor der Manipulation.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 621

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