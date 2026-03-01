---
type: zitat
speaker: "[[Miguel Klauß]]"
date: 2023-01-12
topic: Menschenwürde
page_bfv: 140
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Miguel Klauß]] vom 12.1.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Sinan B. ist der Name des 'Deutschen', der seine Lehrerin getötet hat In Ibbenbüren bei Münster erstach ein Schüler seine Lehrerin. Als Motivation, warum der renitente 17-jährige 'Deutsche' Sinan B. seine Lehrkraft ein Messer in den Leib rannte, wird Rache aufgrund eines Schulverweises vermutet. [...] Warum wird wieder nicht erwähnt, daß der Täter ein Migrationshintergrund hat? Schließlich interessiert das viele - inzwischen weiß jeder, wird die Nationalität von Tätern nicht genannt, gibt es immer ein Migrationshintergrund.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 140

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