---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2022-12-20
topic: Demokratieprinzip
page_bfv: 573
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 20.12.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Die Ampelregierung der US-Statthalter geben alles dafür, dass Deutschland auf allen Ebenen ausblutet. Der ewige Beifall wird vom Staatsfunk propagiert bis niemand mehr diesen Schwachsinn schaut. Sie werden den ewigen 'Nazi'-Popanz ausspielen, bis Deutschland komplett ausgesaugt ist. Der Great Reset ist ihr Ziel. Die Masse ist arglos und scheint geistig wehrlos. Anstatt souverän und selbstbewusst zu handeln, übernimmt man lieber die einfachen Narrative des politmedialen Verbrecherkartells. [...] Doch es rumort in der Gesellschaft, viele wollen dieses Regime nicht mehr stützen und übernehmen teilweise unwissend AfD-Thesen, weil es der klaren Vernunft entspricht, ohne AfD-Wähler zu sein, da helfen auch keine inszenierten Putsche der Antidemokratin Faeser, die nun ihren Überwachungs- und Denunziantenstaat ausweiten will, um die Demokratie nachweislich zu schädigen. Doch in dieser verlumpten West-DDR und mit dieser geistig verwahrlosten, dummdreisten, bis masochistischen Politelite scheint in diesem Land jede totalitäre Geisteshaltung gegen das eigene Land möglich, umgesetzt zu werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 573

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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