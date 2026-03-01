---
type: zitat
speaker: "[[Jan Moldenhauer]]"
date: 2022-06-11
topic: Menschenwürde
page_bfv: 392
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jan Moldenhauer]] vom 11.6.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Großbritannien macht es richtig und schiebt illegale Zuwanderer nach Ruanda ab. Daran sollte sich Deutschland ein Beispiel nehmen. Die kulturfremden jungen Männer müssen zurück nach Afrika geschickt werden, denn dort gehören sie hin.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 392

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