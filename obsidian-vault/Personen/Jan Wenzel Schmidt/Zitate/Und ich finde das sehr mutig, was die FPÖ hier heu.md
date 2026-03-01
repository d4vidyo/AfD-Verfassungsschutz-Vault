---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2023-11-20
topic: Sonstiges
page_bfv: 783
source: 'Podiumsdiskussion'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 20.11.2023 veröffentlicht auf: 'Podiumsdiskussion'
> [!quote] Aussage
>Und ich finde das sehr mutig, was die FPÖ hier heute gemacht hat und dass sie eben auch das Thema Linksextremismus, was auch ein unangenehmes Thema ist, so in den Fokus schieben, und dabei auch das politische Vorfeld einbinden, was ja am längsten schon mit Linksextremismus zu tun hat. Immer wieder werden sie angegriffen und auch immer wieder wird das politische Vorfeld, Identitäre Bewegung und auch andere Institutionen, als rechtsextrem bezeichnet. Aber hier sieht man den großen Unterschied, denn die Identitäre Bewegung fällt nicht mit Gewalt auf, die Linksextremen, vor allem die Antifa, immer wieder.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 783

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