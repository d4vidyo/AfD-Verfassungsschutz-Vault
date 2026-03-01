---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-08-20
topic: Menschenwürde
page_bfv: 362
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 20.8.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die Sozialkassen finanzieren die Migranten - und locken deshalb umso mehr an. Die Deutschen werden im eigenen Land ausgeplündert, um die Einwandetung zu bezahlen, die ihnen Wohlstand und Heimat nimmt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 362

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