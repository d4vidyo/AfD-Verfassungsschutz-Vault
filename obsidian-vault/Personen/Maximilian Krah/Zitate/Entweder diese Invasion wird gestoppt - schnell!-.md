---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-09-18
topic: Menschenwürde
page_bfv: 370
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 18.9.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Entweder diese Invasion wird gestoppt - schnell!- oder Europa ist tot. Die politischen, wirtschaftlichen und kulturellen Eliten bejubeln diesen Untergang, weil sie die eigene Kultur und Herkunft hassen, Deshalb darf man nicht an sie appellieren, sondern muss sie ersetzen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 370

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