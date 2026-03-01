---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-09-16
topic: Sonstiges
page_bfv: 706
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 16.9.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Danke, @tagesschau, dass Sie diese Aussage verbreiten. Sie liegt mir am Herzen. Dass Sie ein unvorteilhaftes Foto verwenden, ist gewiss nur ein Versehen. ‚Wir können nur eine Alternative für Deutschland sein, wenn wir im lebendigen Austausch mit dem Vorfeld sind, einem Austausch unter Gleichrangingen wohlgemerkt. Deshalb gelte für Junge Alternative, Compact oder ‚Ein Prozent‘, für Schnellroda, ‚Pegida‘ oder ‚Zukunft Heimat‘: ‚Wir distanzieren uns nicht! Wir halten zusammen und wehren uns zusammen!‘

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 706

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