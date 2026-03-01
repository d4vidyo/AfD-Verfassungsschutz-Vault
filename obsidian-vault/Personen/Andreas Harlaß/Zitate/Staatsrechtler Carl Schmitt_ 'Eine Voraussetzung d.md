---
type: zitat
speaker: "[[Andreas Harlaß]]"
date: 2022-02-26
topic: Menschenwürde
page_bfv: 127
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Andreas Harlaß]] vom 26.2.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Staatsrechtler Carl Schmitt: 'Eine Voraussetzung der nationalen Demokratie ist nationale Homogenität. Eine Nation ist ein durch politisches Sonderbewußtsein individualisiertes Volk. Zu dessen Einheit und Einheitsbewusstsein tragen verschiedene Elemente bei: Gemeinsame Sprache, gemeinsame geschichtliche Schicksale, Traditionen und Erinnerungen. Gemeinsame politische Ziele und Hoffnungen. Ist in der politischen Wirklichkeit die nationale Homogenität nicht vorhanden, weil ein Staat aus verschiedenen Nationen besteht oder nationale Minderheiten enthält, so ergeben sich verschiedene Lösungsmöglichkeiten: Zunächst der Versuch eines friedlichen Ausgleichs; das bedeutet aber in Wahrheit entweder friedliche Auseinandersetzung und Trennung, oder allmähliche, friedliche Assimilierung an die herrschende Nation.' Die weiteren Ausführungen habe ich bewusst nicht veröffentlicht, sie zögen im Zeitalter der neuen deutschen Meinungskorrektur eine Sperrung nach sich.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 127

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