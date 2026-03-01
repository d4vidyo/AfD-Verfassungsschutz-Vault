---
type: zitat
speaker: "[[Robert Farle]]"
date: 2022-11-11
topic: Menschenwürde
page_bfv: 192
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Robert Farle]] vom 11.11.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wir haben eine Innenministerin Faeser, die Migrationszahlen schönt und den Bevölkerungsaustausch in bester Merkel-Manier vorantreibt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 192

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