---
type: zitat
speaker: "[[Siegbert Droese]]"
date: 2022-09-22
topic: Sonstiges
page_bfv: 763
source: 'None'
status: Unbewertet
---

# Zitat: [[Siegbert Droese]] vom 22.9.2022 veröffentlicht auf: 'None'
> [!quote] Aussage
>Hervorragend! LESEEMPFEHL UNG!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 763

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