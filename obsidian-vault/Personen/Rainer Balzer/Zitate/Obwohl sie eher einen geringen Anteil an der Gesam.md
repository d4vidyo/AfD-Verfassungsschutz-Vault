---
type: zitat
speaker: "[[Rainer Balzer]]"
date: 2022-07-19
topic: Menschenwürde
page_bfv: 457
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Rainer Balzer]] vom 19.7.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Obwohl sie eher einen geringen Anteil an der Gesamtbevölkerung ausmachen, gehören Syrer und Afghanen zu den häufigsten Tätergruppen bei Gewaltdelikten wie Totschlag. Doch wenn Sie unsere rosa-rot-grüne Regierung fragen, dann haben wir natürlich kein Problem mit Ausländerkriminalität. Und natürlich ist für unser Innenministerium, wie wir inzwischen wissen, die AfD wesentlich gefährlicher als tausende islamtreue und gewaltbereite Migranten

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 457

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