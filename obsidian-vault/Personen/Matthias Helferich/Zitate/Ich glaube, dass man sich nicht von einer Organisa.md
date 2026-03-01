---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-11-13
topic: Sonstiges
page_bfv: 780
source: 'Heimatkurier'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 13.11.2023 veröffentlicht auf: 'Heimatkurier'
> [!quote] Aussage
>Ich glaube, dass man sich nicht von einer Organisation distanzieren muss, die friedlich für ähnliche Ziele, wie es auch die AfD auf dem parlamentarischen Parkett tut, eintritt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 780

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