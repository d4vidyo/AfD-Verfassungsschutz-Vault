---
type: zitat
speaker: "[[Franz Schmid]]"
date: 2024-10-31
topic: Sonstiges
page_bfv: 743
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Franz Schmid]] vom 31.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wenn unser Vorfeld angegriffen wird, müssen wir zusammenhalten. Deswegen unterstütze ich die Kampagne des @ein_prozent Solifonds!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 743

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