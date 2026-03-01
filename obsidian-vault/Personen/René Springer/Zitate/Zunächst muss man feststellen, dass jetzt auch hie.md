---
type: zitat
speaker: "[[René Springer]]"
date: 2024-09-23
topic: Menschenwürde
page_bfv: 409
source: 'Deutschlandfunk'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 23.9.2024 veröffentlicht auf: 'Deutschlandfunk'
> [!quote] Aussage
>Zunächst muss man feststellen, dass jetzt auch hier in unserem Gespräch wieder über Dinge gesprochen wird, von denen ich annehme, dass sie die allermeisten Bürger überhaupt nicht interessieren. [...] wir haben ja nun auch in den Wahlen gezeigt, dass, wo übrigens dieser Abschiebesong Teil auch der Kampagne unserer Jugendorganisation war, dass wir damit einen deutlichen Wählerzuwachs erzielen konnten. Und wenn ich so mit den Menschen spreche, am Rande von Wahlveranstaltungen, am Rande von Bürgerdialogen, dann ist es genau, was die Leute wollen. Sie wollen Ordnung haben. Sie wollen, dass das Migrationschaos beendet wird. Und sie wollen, dass abgeschoben wird. [...] Wir reden hier von der Jugendorganisation der AfD. Diese Jugendkultur hat eben eigene Mittel und Wege, um Wähler anzusprechen. Und wenn wir sehen, dass heute ein so großer Teil der Jungwähler sich für die AfD entscheidet, hat das ja offenbar auch gut funktioniert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 409

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