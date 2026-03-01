---
type: zitat
speaker: "[[Eric Engelhardt]]"
date: 2025-02-01
topic: Sonstiges
page_bfv: 870
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Eric Engelhardt]] vom 1.2.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die Junge Alternative ist tot, lang lebe die Junge Alternative.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 870

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