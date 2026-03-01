---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2023-04-26
topic: Sonstiges
page_bfv: 740
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 26.4.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Nun bin ich auch Fördermitglied bei Ein Prozent. Vielen Dank für den Hinweis, Thomas Mecki Haldenwang!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 740

**Verfassungsschutz Kategorisierung:** Sonstiges.

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