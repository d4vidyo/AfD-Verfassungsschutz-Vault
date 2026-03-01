---
type: zitat
speaker: "[[Ulrich Oehme]]"
date: 2021-05-14
topic: Menschenwürde
page_bfv: 345
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Ulrich Oehme]] vom 14.5.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Presse verleugnet afrikanische Wurzeln der Täter ‚aus gutem Hause‘

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 345

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