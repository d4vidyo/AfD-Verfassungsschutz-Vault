---
type: zitat
speaker: "[[Jan Petersen-Brendel]]"
date: 2022-12-11
topic: Menschenwürde
page_bfv: 297
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jan Petersen-Brendel]] vom 11.12.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wer CDU/CSU. SPD, Grün Linke und FDP wählt öffnet den Messermördern die Grenzen

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 297

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