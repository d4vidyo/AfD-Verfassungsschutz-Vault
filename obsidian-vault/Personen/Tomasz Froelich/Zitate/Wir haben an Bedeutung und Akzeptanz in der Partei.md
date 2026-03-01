---
type: zitat
speaker: "[[Tomasz Froelich]]"
date: 2023-08-18
topic: Sonstiges
page_bfv: 831
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Tomasz Froelich]] vom 18.8.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir haben an Bedeutung und Akzeptanz in der Partei gewonnen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 831

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