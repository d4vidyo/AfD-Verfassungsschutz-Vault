---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2022-08-21
topic: Menschenwürde
page_bfv: 153
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 21.8.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Vollkommene Gleichschaltung und Agenda Setting auf allen Ebenen und die globalistischen Medienkartelle und NGO-Verbrecher lachen sich mal wieder schlapp über dieses Land, das ich an manchen Tagen nur noch als gebrochenes Experiment der Siegermächte bezeichnen mag.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 153

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