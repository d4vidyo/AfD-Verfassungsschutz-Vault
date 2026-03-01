---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-09-12
topic: Sonstiges
page_bfv: 741
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 12.9.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Mein patriotisches 'Nest' in Dortmund findet sich nun auch in der Liste der patriotischen Zentren! [...] Hier geht es zum Artikel bei #EinProzent

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 741

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