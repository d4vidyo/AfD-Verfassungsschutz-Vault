---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2021-09-04
topic: Menschenwürde
page_bfv: 501
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 4.9.2021 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Dieses Grundproblem ist die Existenz einer kleinen, superreichen Klasse. Einer kleinen Klasse von [unverständlich] Verdienern, einer kleinen Klasse, die mit Hilfe eines falsch konzipierten Geldsystems den Reichtum der arbeitsamen Bevölkerung seit Jahren und Jahrzehnten abschöpfen und zu ihrem Großkapital denn dazulegen. [...] Ein Großteil der Richter des Europäischen Gerichtshofes, auch das wissen die Wenigsten, ist durch das Netzwerk von George Soros gegangen und dort sozialisiert worden. Angela Merkel, Annalena Baerbock, sind Young Leaderships. Sie sind im [...] Young Leadership-Programm von wem? Klaus Schwab, der Speerspitze der Globalisten. Das sind nur einige Indizien, die dafür sprechen, dass die Superreichen versuchen, informell die Herrschaft in dieser Welt an sich zu reißen, demokratische Strukturen zu unterwandern und letztlich die Volkssouveränität auszuhebeln.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 501

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