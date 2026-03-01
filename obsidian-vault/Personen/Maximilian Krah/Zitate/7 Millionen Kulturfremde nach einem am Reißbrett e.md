---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-11-03
topic: Menschenwürde
page_bfv: 178
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 3.11.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>7 Millionen Kulturfremde nach einem am Reißbrett entworfenen Generalplan in Deutschland anzusiedeln ist keine Einwanderung - das ist Ersetzung, das ist 'Großer Austausch'. Die #AfD ist die einzige Partei, die sich dagegen wehrt - und deshalb schlussendlich auch gewinnen wird!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 178

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