---
type: zitat
speaker: "[[Nicole Hess]]"
date: 2024-02-20
topic: Menschenwürde
page_bfv: 397
source: 'm.osthessen-news.de'
status: Unbewertet
---

# Zitat: [[Nicole Hess]] vom 20.2.2024 veröffentlicht auf: 'm.osthessen-news.de'
> [!quote] Aussage
>Stärkung des Heimatgefühls in der Gemeinde. Die Überfremdung stoppen. Das bedeutet auch, die Mietverträge der Sammelunterkunft zu überprüfen und falls möglich, unter Beachtung aller gesetzlichen Fristen, zu kündigen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 397

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