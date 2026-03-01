---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-11-11
topic: Sonstiges
page_bfv: 779
source: 'Interview'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 11.11.2023 veröffentlicht auf: 'Interview'
> [!quote] Aussage
>Frage: Da ist dann auch die Zusammenarbeit mit Gruppierungen recht, die vom Verfassungsschutz als rechtsextrem oder verfassungsfeindlich eingeschätzt werden? Helferich: Also da hat die AfD große Schwierigkeiten, wenn sie auf die Bewertung des Verfassungsschutzes etwas geben würde, weil es ja die Aufgabe des Bundesamtes für Verfassungsschutz ist, alle rechten Gruppierungen, und seien sie noch so demokratisch, zu kontaminieren, um eben auch diesen Kulturkampf zu behindern. Also unsere Jugendorganisation ist ja in Teilen als Verdachtsfall oder als rechtsextreme Bestrebung eingestuft. Ich hielte nichts davon, sich von der eigenen Jugendorganisation, wie es das Establishment letztlich ja beabsichtigt, zu distanzieren. Auch die AfD ist momentan nach der Rechtsprechung Verdachtsfall, wehrt sich dagegen. Aber es ist... Also ich gebe auf dieses Amt und auch auf Herrn Haldenwang als weisungsgebundenen Spitzenbeamten nichts. Frage: Und als Bundestagsabgeordneter gibt es denn Gruppierungen, von denen Sie sich eindeutig distanzieren würden, beispielsweise die Identitäre Bewegung oder ähnliche im rechten Raum? Helferich: Also es gibt bestimmt Organisationen, mit denen ich keine Kooperation anstreben würde und die ich auch ablehne in ihren Zielvorstellungen. Das gilt für eine Identitäre Bewegung nicht, dass ich mich von denen distanzieren würde, weil ich glaube, dass man sich nicht von einer Organisation distanzieren muss, die friedlich für ähnliche Ziele, wie es auch die AfD auf dem parlamentarischen Parkett tut, eintritt. Herbert Kickl hat das letztens auch ganz klar gesagt, dass letztlich diese Jagd auf die Identitäre Bewegung dadurch begründet war, dass sie eben so erfolgreich war. Sie war eine popkulturelle Bewegung, ästhetisch ansprechend, mutig, auch gleichzeitig sehr smart, durchaus sehr intellektuell, hat ja auch vieles aus den erfolgreichen linken Bewegungen kopiert und deshalb wurde sie auch so massiv innerhalb Europas bekämpft. Letztlich haben ja auch in Österreich die Prozesse gegen die Identitäre Bewegung gezeigt, dass sie, weiß Gott, keine terroristische Vereinigung ist, wie man es versucht hat, ihr zu attestieren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 779. Teile des hier wiedergegebenen Zitats sind Interview-Fragen von SPIEGEL TV.

**Verfassungsschutz Kategorisierung:** Sonstiges.

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