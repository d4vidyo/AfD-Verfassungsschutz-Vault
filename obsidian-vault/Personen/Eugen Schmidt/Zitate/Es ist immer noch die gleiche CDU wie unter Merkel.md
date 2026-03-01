---
type: zitat
speaker: "[[Eugen Schmidt]]"
date: 2024-07-19
topic: Menschenwürde
page_bfv: 464
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Eugen Schmidt]] vom 19.7.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Es ist immer noch die gleiche CDU wie unter Merkel. Diese angeblich christlichkonservative Partei steht für die Islamisierung unseres Landes und unterscheidet sich durch nichts von der Ampel-Koalition.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 464

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