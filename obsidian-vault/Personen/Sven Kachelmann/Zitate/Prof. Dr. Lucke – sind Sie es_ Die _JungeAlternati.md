---
type: zitat
speaker: "[[Sven Kachelmann]]"
date: 2024-12-02
topic: Sonstiges
page_bfv: 863
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Sven Kachelmann]] vom 2.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Prof. Dr. Lucke – sind Sie es? Die #JungeAlternative wird sich jedenfalls nicht auflösen. Wer seine eigene Parteijugend so abschießen will, sollte sein Amt räumen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 863

**Verfassungsschutz Kategorisierung:** Sonstiges.

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