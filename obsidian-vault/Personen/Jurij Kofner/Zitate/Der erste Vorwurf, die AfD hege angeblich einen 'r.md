---
type: zitat
speaker: "[[Jurij Kofner]]"
date: 2023-02-28
topic: Menschenwürde
page_bfv: 129
source: 'freilich-magazin.com'
status: Unbewertet
---

# Zitat: [[Jurij Kofner]] vom 28.2.2023 veröffentlicht auf: 'freilich-magazin.com'
> [!quote] Aussage
>Der erste Vorwurf, die AfD hege angeblich einen 'rein ethnischen Volksbegriff', im Sinne, dass 'nur weiße Deutsche mit deutschen Vorfahren deutsche Staatsbürger werden dürfen', findet weder in AfD-Grundsatzdokumenten und Parteiprogrammen noch in Aussagen der Parteimitglieder eine Bestätigung. Im Gegensatz dazu bekennt sich die blaue Heimatpartei offiziell und 'vorbehaltslos zum deutschen Staatsvolk als der Summe aller Personen, die die deutsche Staatsangehörigkeit besitzen', formuliert dabei gleichzeitig aber auch das klare politische Ziel, die kulturelle Identität des deutschen Volkes in Sprache, Tradition, Werteverständnis und Geschichtserinnerung, also über eine gewisse deutsche Leitkultur, zu bewahren. Zugleich fordert die Partei die Bewahrung eines gewissen ethno-kulturellen Kerns des deutschen Staatsvolkes, also den Erhalt einer ethno-kulturellen deutschen Mehrheit im Staatsvolk. Kein Volk in der Menschheitsgeschichte ist aus dem Nichts entstanden, sondern hat sich dynamisch von Generation zu Generation weiterentwickelt. Die familiären Bindungen von Vorfahren zu Nachkommen sind deshalb nicht unbedeutend für die Weitergabe von kultureller Identität. [...] Somit ist der Volkbegriff der AfD nicht nur vollkommen 'normal', er ist auch eine unabdingbare Voraussetzung für die freiheitlich-demokratische Grundordnung der Bundesrepublik. [...] Weil sozialer Friede in einer echten Demokratie auch eine gewisse ethno-kulturelle Homogenität voraussetzt [...].

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 129

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