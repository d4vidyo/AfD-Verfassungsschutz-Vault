---
type: zitat
speaker: "[[René Springer]]"
date: 2022-09-13
topic: Demokratieprinzip
page_bfv: 548
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 13.9.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Denn es beginnt mit der Einschränkung der Meinungsfreiheit, es beginnt mit der Regulation im Haushalt. Aber es endet irgendwann bei der totalitären Ausgestaltung des Staates, in dem jede Freiheit des Individuums nur noch abhängt von der Willkür der Herrschenden. [...] Das hat dann mit Demokratie nichts mehr zu tun. Und das ist die Gefahr, die ich am Ende dieser Entwicklung sehe, die sich gerade vollzieht. Dass wir am Ende einfach nur noch kleine Teile in einem großen System sind ohne individuelle Freiheit. [...] Aber geopolitisch gesehen, ist die Ukraine momentan das Schlachtfeld eines Stellvertreterkrieges zwischen Russland und den USA. Und dieses Schlachtfeld soll vergrößert werden. [...] Und wenn ich mich zurück erinnere an den Besuch Habecks in den USA, wo er gesagt hat, er sieht Deutschland in einer dienenden Führungsrolle, dann heißt das übersetzt nichts anderes, dass wir hier eine Vasallenregierung haben. Das sind politische Marionetten, die US-Politik umsetzen. [...] Und wir müssen uns aus dieser amerikanischen Umklammerung lösen. Dieser Vasallen-Status, den wir momentan haben, der muss überwunden werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 548

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