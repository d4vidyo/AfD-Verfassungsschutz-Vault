---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2025-01-22
topic: Menschenwürde
page_bfv: 905
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 22.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Diejenigen, die unsere Mädchen und Frauen in Bus und Bahn dumm anmachen, diejenige, die unsere Mädchen und Frauen gruppenvergewaltigen, diejenigen, die kleine Kinder vor den Augen ihrer Eltern vor fahrende Züge werfen, diejenigen, die Menschen mit Macheten in kleine Stücke hacken, diejenigen, die kleine Kinder mit dem Messer niedermetzeln, sie heißen für gewöhnlich nicht Jonas und Tobias, Niklas, Marvin oder Max und Moritz. [...] 25 Messerattacken am Tag in Deutschland statistisch gesehen. Sehr geehrte Anwesende, liebe Mitbürger, die Kartellparteienpolitiker, die haben Deutschland, obwohl wir noch gar nicht im Krieg stehen, Gott sei Dank noch nicht im Krieg stehen mit Russland, sie haben Deutschland in den letzten Jahren und Jahrzehnten zu einem killing field im Frieden gemacht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 905

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