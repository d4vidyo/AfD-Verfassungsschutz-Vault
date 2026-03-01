---
type: zitat
speaker: "[[Martin Renner]]"
date: 2021-12-16
topic: Menschenwürde
page_bfv: 179
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 16.12.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Neben den vaterlandslosen Sozen, die durch unsere reichlich ausgestatteten Sozialkassen all'-überall 'Weltenbummler' – vornehmlich nicht-christlichen Glaubens – anlocken, um dadurch die autochthonen Eingeborenen kurz- bis mittelfristig zu ersetzen und um sich dadurch für spätere Zeiten ein genehmes Wählerkollektiv zu sichern.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 179

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