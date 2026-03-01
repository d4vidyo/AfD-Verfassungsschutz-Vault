---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2022-12-12
topic: Menschenwürde
page_bfv: 176
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 12.12.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Einwanderergesellschaften sind brutal, kriminell und unbarmherzig. Solidarität braucht Homogenität.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 176

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