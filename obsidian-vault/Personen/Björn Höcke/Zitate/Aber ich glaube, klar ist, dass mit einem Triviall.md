---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2023-09-09
topic: Sonstiges
page_bfv: 763
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 9.9.2023 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Aber ich glaube, klar ist, dass mit einem Trivialliberalismus, mit einer mit einer liberal-konservativen Partei, wie sie Lucke vorschwebte, als Juniorpartner für eine CDU, dass wir damit keinen Blumentopf gewonnen hätten. Und dass wir damit, mit diesem Ansatz jetzt in Thüringen nicht bei 34 Prozent ständen. Also, das ist eine parallel gehende weltanschauliche, aber auch strategische Häutung gewesen. Also klare Oppositionsinhalte natürlich mit der Offenheit, die einer angehenden Volkspartei auch gut zu Gesicht steht, aber trotzdem klare Kante. Und dann auch die deutliche Ansage, es gibt keine Alternative im Establishment. Und ich glaube, das ist mittlerweile allgemein das Bewusstsein in der Partei.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 763

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