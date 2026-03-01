---
type: zitat
speaker: "[[Joachim Paul]]"
date: 2022-04-25
topic: Menschenwürde
page_bfv: 471
source: 'Artikel'
status: Unbewertet
---

# Zitat: [[Joachim Paul]] vom 25.4.2022 veröffentlicht auf: 'Artikel'
> [!quote] Aussage
>Das Kölner ,Modellprojekt' war, wie von der AfD bereits befürchtet, nur der Auftakt zu einer bundesweiten Muezzin-Ruf-Offensive, […] Seltsam: im ,Wahl-O-Mat' hat die CDU bei der Frage, ob Moscheegemeinden zum Freitagsgebet rufen dürfen sollten, zugestimmt. Das passt auch zum Verhalten der CDU-Ratsfraktionen in Köln und Koblenz - sie duckten sich beim Thema weg und bahnten oder bahnen so den Weg für diese Machtdemonstrationen. [...] Joachim Paul, Mitglied des AfD-Bundesvorstands: [...] Die Bürger sollten wissen: wer CDU wählt, honoriert politische Rosstäuscher, die das Thema Einwanderung und Integration stets unter den Vorbehalt der Wahlkampftaktik stellen und Probleme und gravierende Fehlentwicklungen wie die Ausbreitung des Islamismus in NRW nicht bekämpfen, sondern moderierend begleiten und die Innere Sicherheit gefährden. Zu Gunsten des Treibens von Hasspredigern und Islamisten. Der Ruf des Muezzins ist eine Demonstration der Macht, er wird von islamistischen Gemeinden zudem als Aufruf zur Durchsetzung einer islamistischen Gesellschaft auf deutschem Boden betrachtet. Er stellt damit in letzter Konsequenz auch Gewaltenteilung, Demokratie und Frauenrechte lautstark in Frage. Die AfD vertritt darüber hinaus die Idee einer deutschen Leitkultur, das heißt: wir bekennen uns selbstverständlich zur freien Religionsausübung, lehnen aber hierfür nicht unabdingbar notwendige lautstarke religiöse Machtdemonstrationen ab. Deshalb bleibt es für die AfD heute und morgen dabei: Kein Ruf des Muezzins in unseren Städten!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 471

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