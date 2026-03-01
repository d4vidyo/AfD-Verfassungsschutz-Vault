---
type: zitat
speaker: "[[Torben Braga]]"
date: 2024-08-26
topic: Menschenwürde
page_bfv: 315
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Torben Braga]] vom 26.8.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>\<Video\> Die Wetteraussichten: [drei Messer-Emojis]

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 315

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