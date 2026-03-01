---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-10-30
topic: Sonstiges
page_bfv: 779
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 30.10.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ernst Moritz Arndt bleibt! Doch die patriotische Gegenöffentlichkeit nimmt die nationale Selbstauflösung durch die Linken nicht hin. Die Bonner AfD machte zusammen mit dem Bundestagsabgeordneten Matthias Helferich über Medien auf die linken Bilderstürmer aufmerksam. Gleichzeitig organisierte die patriotische Jugendorganisation 'Revolte Rheinland' einen Infostand vor der Schule, um die Schüler über Arndt und den linken Kulturkampf gegen ihn aufzuklären.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 779

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