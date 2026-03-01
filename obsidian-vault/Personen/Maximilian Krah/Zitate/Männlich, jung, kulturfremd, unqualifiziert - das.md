---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2022-11-24
topic: Menschenwürde
page_bfv: 385
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 24.11.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Männlich, jung, kulturfremd, unqualifiziert - das ist die Einwanderung, die seit 2015 von CDU, SPD, FDP und Grünen forciert wird. Sie wollen Deutschland abschaffen. Nur die AfD steht dagegen - und wird deshalb dämonisiert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 385

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