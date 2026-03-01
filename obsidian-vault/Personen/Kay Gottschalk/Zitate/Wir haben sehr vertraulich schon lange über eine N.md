---
type: zitat
speaker: "[[Kay Gottschalk]]"
date: 2024-12-03
topic: Sonstiges
page_bfv: 858
source: 'Phoenix'
status: Unbewertet
---

# Zitat: [[Kay Gottschalk]] vom 3.12.2024 veröffentlicht auf: 'Phoenix'
> [!quote] Aussage
>Wir haben sehr vertraulich schon lange über eine Neustrukturierung, einen Reformprozess innerhalb der JA gesprochen. Also insoweit kann auch nicht die Rede sein, dass wir uns von einer Jugendorganisation trennen wollen. Wir brauchen die Jugend. Die Jugend ist gut.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 858. Interview mit Phoenix, das auch auf YouTube veröffentlicht wurde.

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