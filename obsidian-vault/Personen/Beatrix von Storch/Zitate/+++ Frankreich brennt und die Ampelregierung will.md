---
type: zitat
speaker: "[[Beatrix von Storch]]"
date: Nicht Verfügbar
topic: Menschenwürde
page_bfv: 274
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Beatrix von Storch]] vom None veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>+++ Frankreich brennt und die Ampelregierung will weiter Migrantengewalt importieren +++ [...] Die Bürger in Deutschland wollen keine französischen Zustände, sondern ein normales, friedliches Leben wie unsere polnischen Nachbarn - ohne No-Go-Areas und ohne Gewaltimport aus Afrika.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 274

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