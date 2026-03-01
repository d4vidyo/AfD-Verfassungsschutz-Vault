---
type: zitat
speaker: "[[Matthias Moosdorf]]"
date: 2023-01-03
topic: Menschenwürde
page_bfv: 364
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Moosdorf]] vom 3.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Deutschland auf dem Weg zum Shithole-country. Fachkräfte, das Gold aus den Schiffen, sucht man hier vergebens.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 364

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