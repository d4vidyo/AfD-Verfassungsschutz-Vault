---
type: zitat
speaker: "[[Carlo Clemens]]"
date: 2024-12-17
topic: Sonstiges
page_bfv: 861
source: 'Freilich Magazin'
status: Unbewertet
---

# Zitat: [[Carlo Clemens]] vom 17.12.2024 veröffentlicht auf: 'Freilich Magazin'
> [!quote] Aussage
>Hauptgrund ist der Schutz der Jugendorganisation vor einem Vereinsverbot. Auch wenn gerne darauf verwiesen wird, dass Bundesinnenministerin Faeser selbst im Innenausschuss betont hat, dass die JA unter den Schutz des Parteienprivilegs falle, kann ich nur davor warnen, den Worten politischer Gegner blind zu vertrauen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 861

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