---
type: zitat
speaker: "[[Martin Renner]]"
date: 2025-01-13
topic: Demokratieprinzip
page_bfv: 958
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 13.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Allen 'System-Pfuschern' der 'Neuen Sozialistischen Einheitspartei Deutschlands' (NSED) und des polit-ökonomisch-medialen Machtkartells sei lächelnd gesagt: "Ihr erlebt gerade Euer blaues Wunder." Und - Euch zur Erinnerung: Blau ist die Farbe der 'Alternative für Deutschland'

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 958

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