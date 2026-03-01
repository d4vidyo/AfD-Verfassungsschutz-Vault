---
type: zitat
speaker: "[[René Springer]]"
date: 2024-09-23
topic: Sonstiges
page_bfv: 841
source: 'Deutschlandfunk'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 23.9.2024 veröffentlicht auf: 'Deutschlandfunk'
> [!quote] Aussage
>Wir haben ja nun auch in den Wahlen gezeigt, dass, wo übrigens dieser Abschiebesong Teil auch der Kampagne unserer Jugendorganisation war, dass wir damit einen deutlichen Wählerzuwachs erzielen konnten. [...]. Wir reden hier von der Jugendorganisation der AfD. Diese Jugendkultur hat eben eigene Mittel und Wege, um Wähler anzusprechen. Und wenn wir sehen, dass heute ein so großer Teil der Jungwähler sich für die AfD entscheidet, hat das ja offenbar auch gut funktioniert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 841

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