---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2023-12-18
topic: Menschenwürde
page_bfv: 447
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 18.12.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und mindestens genauso grotesk ist die Ablehnung unserer deutschen Kultur durch muslimische Migranten. Sie kommen aus völlig verarmten, dysfunktionalen, von Glaubenskriegen zerrütteten Ländern zu uns hierher. Sie leben hier von der Leistungsfähigkeit unserer aufgeklärten, christlich geprägten und demokratischen Gesellschaft. Und gleichzeitig wollen sie hier ihre Kultur errichten, die ihre Heimatländer in Armut, in Krieg und in Unfreiheit hält. Das ist doch religiöser Wahnsinn. Das ist als Massenphänomen nicht integrierbar. Das ist der heutige Islam und diesem religiösen Wahn müssen wir uns als Gesellschaft mit aller Kraft entgegenstellen. [...] Der heutige real. existierende Islam integriert sich nicht. Der heutige real existierende Islam hat auch nicht die Absicht, sich zu integrieren. Im Gegenteil. In den, wie Pilze aus dem Boden schießenden, Moscheen wird in Deutschland der Unterschied, die Ungleichheit von Mann und Frau vorgebetet. Es wird der Herrschaftsanspruch des Islam und die Minderwertigkeit anderer Religionen vorgebetet. Ich sage, es ist für uns nicht hinnehmbar, wenn die Hälfte der muslimischen Migranten sagt, dass die Scharia über dem Grundgesetz steht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 447

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