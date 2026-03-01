---
type: zitat
speaker: "[[Anna Leisten]]"
date: 2024-07-16
topic: Sonstiges
page_bfv: 714
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Anna Leisten]] vom 16.7.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Egal ob in Amerika oder Falkensee: wir werden weiterkämpfen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 714

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