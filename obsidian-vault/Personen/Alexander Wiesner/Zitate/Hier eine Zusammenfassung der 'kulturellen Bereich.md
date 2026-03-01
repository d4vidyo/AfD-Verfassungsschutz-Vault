---
type: zitat
speaker: "[[Alexander Wiesner]]"
date: 2021-08-09
topic: Menschenwürde
page_bfv: 295
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Alexander Wiesner]] vom 9.8.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Hier eine Zusammenfassung der 'kulturellen Bereicherung' von Migranten seit 2015

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 295

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