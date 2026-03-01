---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2022-08-18
topic: Sonstiges
page_bfv: 704
source: 'YouTube, Kanal "Matthias Helferich MdB"'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 18.8.2022 veröffentlicht auf: 'YouTube, Kanal "Matthias Helferich MdB"'
> [!quote] Aussage
>Ich hoffe, dass hier in Nordrhein-Westfalen ja eine kleine patriotische Festung entsteht, wo gesellschaftliches Leben und politisches Leben vereint werden kann. In rund neunzig Quadratmeter, die wir haben, sollen vor allem zukünftig am stabilsten Tresen von ganz Deutschland nette Tresenabende stattfinden. Über dem Tresen herrscht wirklich noch der Geist der Meinungsfreiheit. Hier sollen Seminare stattfinden, politischer Austausch, aber natürlich auch ne Anlaufstelle für Bürger, die gerade in diesen Krisenzeiten Anliegen haben und diese an mich als Abgeordneten herantragen können.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 704

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