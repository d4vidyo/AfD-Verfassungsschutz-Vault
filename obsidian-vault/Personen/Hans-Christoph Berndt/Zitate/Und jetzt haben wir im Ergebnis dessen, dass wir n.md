---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2022-10-31
topic: Menschenwürde
page_bfv: 512
source: 'AUF1'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 31.10.2022 veröffentlicht auf: 'AUF1'
> [!quote] Aussage
>Und jetzt haben wir im Ergebnis dessen, dass wir nicht nur unter dem Corona-Diktat leiden bis heute in Deutschland und in Österreich, sondern eben auch zunehmend spüren die Folgen dieser Politik, die auf die 'Große Transformation' zielt. Das ist nicht nur Gerede, es geht wirklich darum, dass unsere Art zu leben und wirtschaften ganz anders werden soll, wie es Angela Merkel im Jahr 2020 angekündigt hat. [...] Ja das ist eine Transformation, die dann tatsächlich dazu führt, dass wirklich alles umgestülpt wird, insofern könnte man dann auch fast auch von Revolution sprechen. Und das ist ja auch eine längerfristig angesetzte Politik, die verfolgt längerfristige Ziele oder ist zumindest wirklich strategisch auch angelegt. Und das was wir 2015 erlebt haben mit der Grenzöffnung, mit dieser Migration habe ich spontan damals verstanden als Angriff auf die europäischen Nationalstaaten, auf die Nationalstaaten des weißen Mannes, in Amerika ist es ja nicht viel anders, in den USA. Und tatsächlich, das gehört in den ganzen Zusammenhang der Transformation. Wir haben dann den UNO-Migrationspakt und wir haben eben das Bestreben, nationalstaatliche Ordnung, nationalstaatliche Regelungen abzulösen, durch globale, durch den UNO-Migrationspakt aber auch durch die WHO, das sind dann nicht mehr staatliche Organisationen, sondern das ist eine Mischung von staatlich und privat und zielt wirklich darauf ab, unsere ganze Lebensweise komplett zu ändern. Diese Transformation ist tiefgreifend und da könnte man dann auch schon von Revolution sprechen. [...] Wir sind in der Situation, dass wir von sehr reichen und sehr einflussreichen und mächtigen Leuten, dass sehr einflussreiche und mächtige Leute die Transformation wollen, dass wir nicht mehr so leben, wie wir es gewohnt sind, nicht mehr in Nationalstaaten leben, nicht mehr frei leben, sondern in einer, ich würde mal sagen maoistischen Weltkommune leben, so, wie die es für richtig halten. Das ist die Lage, und dagegen muss man sich wehren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 512

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