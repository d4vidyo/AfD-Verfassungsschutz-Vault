---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2021-11-16
topic: Menschenwürde
page_bfv: 343
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 16.11.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wir brauchen keine sicheren Häfen, sondern sichere Städte ohne Gruppenvergewaltigungen und Messerangriffe!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 343

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