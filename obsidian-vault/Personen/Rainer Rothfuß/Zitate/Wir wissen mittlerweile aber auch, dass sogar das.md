---
type: zitat
speaker: "[[Rainer Rothfuß]]"
date: 2024-12-08
topic: Demokratieprinzip
page_bfv: 949
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Rainer Rothfuß]] vom 8.12.2024 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Wir wissen mittlerweile aber auch, dass sogar das State Department in den USA eingreift, Personal unterhält, auch Mittel bereitstellt, um die AfD möglichst als politische Kraft in Deutschland klein zu halten. Was ist der Grund? Deutschland soll ja unsouverän bleiben, soll ja weiterhin eben den Interessen Brüssels und Washingtons dienen können und das geht eben nur mit Parteien, die diesen Schwur gesprochen haben, alles für Brüssel, alles für Washington. Und da sind wir außen vor. Und das muss man eben auch immer mit einbeziehen. In dieser innenpolitischen Situation spielt eben die geopolitische Interessenlage mit rein. Deutschland darf, soll nicht souverän werden. Das würden wir mit der AfD als Deutschland sicherlich werden. Deswegen diese Einflussnahme.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 949

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