---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2024-01-19
topic: Menschenwürde
page_bfv: 382
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 19.1.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die #Niederlande sind nicht mehr die Niederlande, so @geertwilderspw. Das kann man auch zum überfremdeten #Deutschland konstatieren. Die illegale #Migration zerstört #Europa und führt zu fremd im eigenen Land, aber die #EU handelt nicht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 382

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