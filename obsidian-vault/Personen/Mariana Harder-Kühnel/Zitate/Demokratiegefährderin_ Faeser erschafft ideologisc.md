---
type: zitat
speaker: "[[Mariana Harder-Kühnel]]"
date: 2022-07-04
topic: Demokratieprinzip
page_bfv: 627
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Mariana Harder-Kühnel]] vom 4.7.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Demokratiegefährderin: Faeser erschafft ideologisches Propagandaministerium! Bundesinnenministerin Nancy Faeser (SPD) hat Horst Seehofers Heimatministerium nach eigenen Angaben "umgebaut und verstärkt". [...] Ehrlicher wäre allerdings die Bezeichnung "Propagandaministerium". Denn verfolgt wird unter dem Deckmantel des "gesellschaftlichen Zusammenhalts" einzig das Ziel, eigene Ideologien zu verbreiten und unliebsame Meinungen zu unterdrücken. Große Teile der Gesellschaft werden schon jetzt in den unterschiedlichsten politischen Bereichen diskreditiert und in die Nähe des Extremismus gerückt. [...] Faesers Abteilung zur "Stärkung der Demokratie" ist deshalb nichts anderes als der nächste Baustein zur Abschaffung der Meinungsfreiheit. Die stets geforderte "Meinungsvielfalt" endet für Politiker der Ampelkoalition nämlich stets dort, wo sich geäußerte Meinungen nicht mit den von der Regierung propagierten Ideologien decken.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 627

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