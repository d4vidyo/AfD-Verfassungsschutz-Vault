---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-08-23
topic: Menschenwürde
page_bfv: 178
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 23.8.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Der Große Austausch ist für jedermann sichtbar, tagtäglich. Die Realität zur Verschwörungstheorie zu erklären ist totalitär.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 178

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