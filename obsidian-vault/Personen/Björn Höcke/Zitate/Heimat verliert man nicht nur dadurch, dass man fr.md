---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2025-01-11
topic: Menschenwürde
page_bfv: 883
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 11.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Heimat verliert man nicht nur dadurch, dass man fremd im eigenen Land wird oder zur Flucht und Vertreibung gezwungen wird. Heimat verliert man auch dadurch, dass die Heimat verstellt wird, dass die Identifikation mit dem Landschaftsgefüge der Heimat nicht mehr möglich wird. Und das ist das, was Windindustrieanlagen Deutschland verursachen. Wir verlieren unsere Heimat dadurch, dass wir uns nicht mehr mit unserer Heimat identifizieren können.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 883

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