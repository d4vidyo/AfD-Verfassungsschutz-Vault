---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2024-05-17
topic: Menschenwürde
page_bfv: 501
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 17.5.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>So geht nationale Selbstentmachtung zugunsten eines Clubs der globalen Eliten, in den sich die Reichsten der Superreichen per Spende einkaufen können.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 501

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