---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2024-05-17
topic: Nationalsozialismus
page_bfv: 694
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 17.5.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Aber ich muss eins sagen: ich glaube, dass der Björn Höcke gar nicht 'Alles für Deutschland' gesagt hat, sondern 'Alice für Deutschland'. Da wäre eigentlich alles völlig... [Applaus] [Weidel lacht]. Und daran hatten sie jetzt wahrscheinlich gar nicht gedacht. Mensch, so, jetzt ist das ganze Ding durch. Aber das ist schon unglaublich albern, was hier in diesem Land eigentlich gerade so zugeht. Ich möchte gerne mal eine Liste haben der Sätze, die man noch sagen darf. [...] Dementsprechend ist das ganze natürlich extrem albern, was hier passiert. Aber dummerweise eben auch sehr gefährlich weil ja hier die Meinungsfreiheit eingeschränkt wird.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 694

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