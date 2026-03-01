---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2021-09-17
topic: Sonstiges
page_bfv: 749
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 17.9.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Eine uns sehr wohlgesonnene Bürgerinitiative ist nun dabei, diese Solidarität zu organisieren. Es soll nicht weiter dem Zufall überlassen bleiben, ob ein Fall öffentliche Bekanntheit erlangt und damit auch Hilfswillige erreicht. [...] Anwaltskosten, Öffentlichkeitsarbeit oder Geld für ein ausgebranntes Auto: Die neue Initiative Solifonds hilft, wenn es einen von uns trifft. Unterstützen Sie deshalb Solifonds - mit Spenden, aber auch, indem sie diese Initiative bekannt machen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 749

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