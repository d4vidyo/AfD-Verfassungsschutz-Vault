---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2022-08-25
topic: Menschenwürde
page_bfv: 373
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 25.8.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die erst auf den zweiten Blick freundlichen Herren aus dem Morgenland haben recht: Sie übernehmen den Laden egal, ob [Dänemark-Flagge], [Schweden-Flagge], [Deutschland-Flagge] usw. Sie übernehmen alles, weil wir sie es tun lassen. So einfach ist das.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 373

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