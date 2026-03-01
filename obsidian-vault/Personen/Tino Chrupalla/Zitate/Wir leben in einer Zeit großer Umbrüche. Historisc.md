---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2023-05-11
topic: Nationalsozialismus
page_bfv: 685
source: 'Sezession'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 11.5.2023 veröffentlicht auf: 'Sezession'
> [!quote] Aussage
>Wir leben in einer Zeit großer Umbrüche. Historische Schuld sollte unser Handeln nicht länger bestimmen. Irgendwann wird der russische Botschafter zu unserer Gedenkfeier kommen. Das ist Teil meiner Arbeit für die beiderseitige Aussöhnung.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 685

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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