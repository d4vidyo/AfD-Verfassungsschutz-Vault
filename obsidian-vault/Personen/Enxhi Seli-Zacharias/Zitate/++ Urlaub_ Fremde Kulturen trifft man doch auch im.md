---
type: zitat
speaker: "[[Enxhi Seli-Zacharias]]"
date: 2022-06-23
topic: Menschenwürde
page_bfv: 390
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Enxhi Seli-Zacharias]] vom 23.6.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>++ Urlaub? Fremde Kulturen trifft man doch auch im Freibad ++ Früher musste man als Deutscher nach Nordafrika fliegen, um zu erleben, wie ungezwungen Männer dort mit ihrem Testosteron umgehen. Und um zu bestaunen, wie anders patriarchalische Strukturen das Verständnis von Männlichkeit prägen, bereiste man neugierig den arabischen Raum. 'Heute reicht dafür ein Besuch im nächsten Freibad', kommentiert unsere integrationspolitische Sprecherin, Enxhi Seli-Zacharias, in Anbetracht der jüngsten Freiluft-Massenschlägerei unter rund einhundert 'jungen Männern' in Berlin. 'Die Deutschen haben zwar nicht danach verlangt, diese Kulturkreise in Scharen in ihr Land zu holen, aber, wie sagte es Merkel doch gleich? Jetzt sind sie halt da.'

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 390

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