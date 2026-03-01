---
type: zitat
speaker: "[[Arthur Hammerschmidt]]"
date: 2025-01-14
topic: Sonstiges
page_bfv: 868
source: 'Heilbronner Stimme'
status: Unbewertet
---

# Zitat: [[Arthur Hammerschmidt]] vom 14.1.2025 veröffentlicht auf: 'Heilbronner Stimme'
> [!quote] Aussage
>Wir sehen keinen großen Unterschied im Arbeiten zwischen dem Zustand vor dem Parteitagsbeschluss und dem Arbeiten in der künftigen Jugendorganisation.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 868

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