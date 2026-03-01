---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-03-27
topic: Menschenwürde
page_bfv: 417
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 27.3.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die einzig richtige Aktion gegen das erste arabischsprachige Straßenschild Deutschlands, die Ellerstraße in Düsseldorf. mehr Karl Martell wagen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 417. dazu Bild eines von rechtsextremistischen Aktivisten mit "Karl-Martell-Straße" überklebten zusätzlichen arabischen Straßenschildes

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