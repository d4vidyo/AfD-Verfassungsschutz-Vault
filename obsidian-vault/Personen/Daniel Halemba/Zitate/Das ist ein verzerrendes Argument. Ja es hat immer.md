---
type: zitat
speaker: "[[Daniel Halemba]]"
date: 2023-11-01
topic: Menschenwürde
page_bfv: 214
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Daniel Halemba]] vom 1.11.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Das ist ein verzerrendes Argument. Ja es hat immer Migration gegeben, die unterscheidet sich aber massiv von modernen, globalen Wanderbewegungen. Noch nie wurde eine Bevölkerung so schnell ausgetauscht wie heute, es sei denn es handelte sich um eine Eroberung mit Genozid.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 214

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