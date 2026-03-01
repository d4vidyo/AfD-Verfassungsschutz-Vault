---
type: zitat
speaker: "[[Steffen Kotré]]"
date: 2022-04-08
topic: Sonstiges
page_bfv: 796
source: 'PI-NEWS'
status: Unbewertet
---

# Zitat: [[Steffen Kotré]] vom 8.4.2022 veröffentlicht auf: 'PI-NEWS'
> [!quote] Aussage
>Schön, dass also hier jetzt so ein Blog existiert, hier so ein Medium, PI-NEWS, das wirklich unabhängig berichten kann.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 796

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