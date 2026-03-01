---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2023-05-08
topic: Menschenwürde
page_bfv: 245
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 8.5.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Deutschland ist heutzutage vielerorts in Politik und Medien zu einem unentrinnbaren Schuldzusammenhang geschrumpft, der als einzigen Ausweg die Auflösung der Nation kennt. Eine solche Fixierung nur auf einen Teil der Geschichte führt aber zu einem Realitätsverlust für Vergangenheit und auch Gegenwart und letztlich zu einer autoaggressiven Landschaft, in der keine Zugehörigkeit zum Eigenen entstehen und bestehen kann.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 245

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