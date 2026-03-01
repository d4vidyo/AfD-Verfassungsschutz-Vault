---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2024-12-03
topic: Sonstiges
page_bfv: 858
source: 'Presserklärung'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 3.12.2024 veröffentlicht auf: 'Presserklärung'
> [!quote] Aussage
>Vielleicht ergänzend, weil das teilweise ja auch falsch in den Medien dargestellt wird, dass der AfD-Bundesvorstand die JA loswerden möchte oder auflösen möchten, also das ist mitnichten der Fall. Des Weiteren geht das überhaupt nicht, die AfD-Mutterpartei kann eine Jugendorganisation, noch dazu die JA gar nicht auflösen. Das könnte sie nur im Ernstfall selbst tun, weil das ein eigenständiger Verein ist. Und so wie es auch gerade erwähnt wurde, die JA hat dort selbst eine sehr gute Vorarbeit geleistet in der Umstrukturierung und das wird auch Bestandteil eines Antrages auf dem Bundesparteitag sein.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 858

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