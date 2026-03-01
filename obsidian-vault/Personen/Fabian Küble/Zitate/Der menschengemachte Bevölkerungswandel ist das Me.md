---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2024-07-09
topic: Menschenwürde
page_bfv: 196
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 9.7.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Der menschengemachte Bevölkerungswandel ist das Menschheitsverbrechen des 21. Jahrhunderts.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 196

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