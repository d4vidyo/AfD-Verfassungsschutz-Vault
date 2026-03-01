---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2023-08-27
topic: Menschenwürde
page_bfv: 211
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 27.8.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Uns immer wieder vorgeworfen, wir sprechen vom 'Großen Austausch'. [...] Auf Englisch: Replacement Migration. [...] Das ist nichts anderes als ein Austausch, eine Ersetzungsmigration. Genau dazu hat uns Merkel bereits vor Jahren verpflichtet.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 211

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