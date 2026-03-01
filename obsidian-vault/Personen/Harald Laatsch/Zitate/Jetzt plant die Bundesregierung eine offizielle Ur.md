---
type: zitat
speaker: "[[Harald Laatsch]]"
date: 2024-12-20
topic: Demokratieprinzip
page_bfv: 963
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Harald Laatsch]] vom 20.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Jetzt plant die Bundesregierung eine offizielle Urlaubsreiseerlaubnis für Menschen die angeblich aus dem Land "flüchten" mussten. Deutschland ist ein Unrechtsstaat gegen seine eigene Bevölkerung. Damit das so bleibt haben sich die Täter das Bundesverfassungsgericht gesichert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 963

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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