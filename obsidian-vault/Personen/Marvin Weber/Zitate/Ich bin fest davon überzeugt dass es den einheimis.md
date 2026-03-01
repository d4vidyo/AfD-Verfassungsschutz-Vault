---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2022-07-26
topic: Nationalsozialismus
page_bfv: 683
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 26.7.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Ich bin fest davon überzeugt dass es den einheimischen Deutschen auf der Seele brennt endlich wieder ohne ewigen Schuldkult Deutsche im eigenen Land sein zu dürfen – und zwar stolz und tugendhaft, ohne sich einer sich diskriminiert fühlenden Minderheit von Diskriminierern und antideutschen Rassisten und ein gewanderten Faschisten unterzuordnen. Wir wollen endlich wieder frei von den ewigen Ketten der ewigen Geschichtsinstrumentalisierung der uns ausplündernden Staaten sein. Wir sind die friedlichen Nachkriegsgenerationen und lassen uns nicht mehr entmüdigen, entrechten oder versklaven. [...] Eure Nazikeule, die ihr inflationär und geschichtsrelativierend gegenüber uns nutzt ist das Abscheulichste und Erbärmlichste, was ich jemals gehört habe.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 683. abweichendes Datum in der Fußnote des Berichts

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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