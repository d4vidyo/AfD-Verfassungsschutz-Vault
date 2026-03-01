---
type: zitat
speaker: "[[Paul Timm]]"
date: 2022-12-27
topic: Menschenwürde
page_bfv: 382
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Paul Timm]] vom 27.12.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>\<Bild MISSION ERFÜLLT – DEUTSCHLAND KAPUTT\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 382. zu einem Post auf Seite 381, zu sehen sind Annalena Baerbock und Robert Habeck

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