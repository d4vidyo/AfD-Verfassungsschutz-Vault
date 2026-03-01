---
type: zitat
speaker: "[[Alexander Wiesner]]"
date: 2024-05-30
topic: Demokratieprinzip
page_bfv: 595
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Alexander Wiesner]] vom 30.5.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>\<Bild Ab jetzt nur noch Demokratie wählen! Ihre Einheitspartei.\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 595

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