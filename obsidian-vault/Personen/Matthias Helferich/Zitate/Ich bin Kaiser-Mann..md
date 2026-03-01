---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2024-07-21
topic: Sonstiges
page_bfv: 761
source: 'Instagram'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 21.7.2024 veröffentlicht auf: 'Instagram'
> [!quote] Aussage
>Ich bin Kaiser-Mann.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 761

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