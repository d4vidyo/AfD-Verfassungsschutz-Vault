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
>[W]ir spüren die Folgen dieser Politik, die auf die 'Große Transformation' zielt. Das ist nicht nur Gerede, es geht wirklich darum, dass unsere Art zu leben und zu wirtschaften ganz anders werden soll, wie es Angela Merkel im Jahr 2020 angekündigt hat. [...] Ja das ist eine Transformation, die dann dazu führt, dass wirklich alles umgestülpt wird, insofern könnte man dann auch fast auch von Revolution sprechen. Und das ist ja auch eine längerfristig angesetzte Politik, sie verfolgt längerfristige Ziele oder ist zumindest wirklich strategisch auch angelegt. Und das, was wir 2015 erlebt haben mit der Grenzöffnung, mit dieser Migration, habe ich spontan damals verstanden als Angriff auf die europäischen Nationalstaaten, auf die Nationalstaaten des weißen Mannes.

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