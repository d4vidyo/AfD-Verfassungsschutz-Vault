---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-01-14
topic: Menschenwürde
page_bfv: 364
source: 'YouTube, Kanal Schnellroda'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 14.1.2023 veröffentlicht auf: 'YouTube, Kanal Schnellroda'
> [!quote] Aussage
>Sie sind deshalb da, weil sie anstrengungslos Geld bekommen durch den Sozialstaat und sie sind hier da, weil sie eine gewisse sexuelle Libertinage und auch eine strafrechtliche Libertinage in Anspruch nehmen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 364

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