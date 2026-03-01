---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-07-28
topic: Menschenwürde
page_bfv: 211
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 28.7.2023 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Aber es ist so, dass wir natürlich eine Ersetzungsmigration erleben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 211

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