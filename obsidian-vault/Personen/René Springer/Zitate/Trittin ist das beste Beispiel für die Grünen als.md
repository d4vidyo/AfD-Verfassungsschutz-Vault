---
type: zitat
speaker: "[[René Springer]]"
date: 2024-09-08
topic: Menschenwürde
page_bfv: 249
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 8.9.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Trittin ist das beste Beispiel für die Grünen als ideologische PR-Abteilung eines enthemmten Neoliberalismus. Eine Nation ist mehr als Humankapitallager und Spielwiese für Konzerne. Ostdeutschland konnte die Mangelwirtschaft der DDR überstehen, aber Massenmigration und das 'Vielfalt'-Gesellschaftsexperiment sind eine reale Existenzgefahr, und zwar für das ganze Land, denn wenn am Ende hier nicht mehr dieselben Menschen leben, dann ist dies auch nicht mehr Deutschland. Und es ist das Geburtsrecht der Deutschen, so einen Prozess des Heimatverlustes abzulehnen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 249

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