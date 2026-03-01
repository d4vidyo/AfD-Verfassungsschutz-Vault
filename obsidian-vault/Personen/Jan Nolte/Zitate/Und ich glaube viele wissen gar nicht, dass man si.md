---
type: zitat
speaker: "[[Jan Nolte]]"
date: 2023-04-22
topic: Menschenwürde
page_bfv: 157
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jan Nolte]] vom 22.4.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Und ich glaube viele wissen gar nicht, dass man sich schon in ganz gefährliche Fahrwasser begibt, wenn man überhaupt sagt, dass es ein deutsches Volk gibt. Also wenn man nicht sagt, dass es besser als andere Völker, sondern wenn man nur sagt, das gibt es. Oder wenn man sagt, es gibt natürlich - also wer die deutsche Staatsbürgerschaft hat, natürlich, der gehört zum deutschen Staatsvolk. Aber es gibt gleichzeitig noch ein historisch gewachsenes Volk, das seine Tradition hat, wo man sich natürlich auch ein fügen kann, über die Zeit, gar keine Frage. Und assimilieren kann, Teil davon werden kann, aber das ist noch mal was anderes.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 157

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