---
type: zitat
speaker: "[[Ulrich Oehme]]"
date: 2023-10-04
topic: Menschenwürde
page_bfv: 173
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Ulrich Oehme]] vom 4.10.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Illegale Einwanderung führt nicht nur zur Aufweichung unserer deutschen Kultur und Identität, sondern auch zum Ausbluten der Sozialsysteme. [...] Deutschland kann nur durch eine Regierung gerettet werden, die sich endlich den Problemen und Sorgen des eigenen Volkes widmet und sich nicht um das Ansehen auf dem internationalen Parkett kümmert. Ein zentraler Faktor dabei ist und bleibt die sofortige Remigration, um unsere ethnokulturelle Identität zu schützen und zu bewahren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 173

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