---
type: zitat
speaker: "[[Christina Baum]]"
date: 2023-11-03
topic: Menschenwürde
page_bfv: 209
source: 'www.afd.de'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 3.11.2023 veröffentlicht auf: 'www.afd.de'
> [!quote] Aussage
>Wir müssen eines in aller Deutlichkeit feststellen: Die überwiegend illegale Massenmigration nach Deutschland ist nicht zufällig über Nacht über uns gekommen. Sie ist ein schon vor dem Jahr der Grenzöffnung 2015 generalstabsmäßig gefasster Plan, um die alternde deutsche Gesellschaft durch arbeitsfähige Migranten zu ersetzen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 209

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