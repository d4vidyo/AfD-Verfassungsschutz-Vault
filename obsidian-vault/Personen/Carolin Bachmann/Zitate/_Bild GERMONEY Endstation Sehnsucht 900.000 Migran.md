---
type: zitat
speaker: "[[Carolin Bachmann]]"
date: 2023-04-14
topic: Menschenwürde
page_bfv: 380
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Carolin Bachmann]] vom 14.4.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>\<Bild GERMONEY Endstation Sehnsucht 900.000 Migranten starten ihren TRIP ins Glück INVASOREN sorgen für einen heißen Sommer\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 380

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