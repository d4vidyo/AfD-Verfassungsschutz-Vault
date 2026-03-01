---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2023-09-18
topic: Menschenwürde
page_bfv: 322
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 18.9.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Deutsche Frauen und Mädchen gelten inzwischen als Freiwild für enthemmte Männerhorden. Eine Bundesregierung, die vollständig darauf verzichtet, Kontrolle auszuüben und unter deren 'Führung‘ solche Taten praktisch folgenlos bleiben, macht diese ekelhaften Zustände erst möglich.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 322

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