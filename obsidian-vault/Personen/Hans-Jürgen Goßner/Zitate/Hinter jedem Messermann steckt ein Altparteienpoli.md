---
type: zitat
speaker: "[[Hans-Jürgen Goßner]]"
date: 2025-01-23
topic: Menschenwürde
page_bfv: 914
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Hans-Jürgen Goßner]] vom 23.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Hinter jedem Messermann steckt ein Altparteienpolitiker, der ihn eingeladen hat! #Aschaffenburg #Remigration“

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 914

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