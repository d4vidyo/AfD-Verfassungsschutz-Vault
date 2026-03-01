---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-01-31
topic: Sonstiges
page_bfv: 764
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 31.1.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Egal, ob man dem Autor in allen Punkten folgt oder nicht: dieses Buch ist die Lektüre der Stunde für jeden oppositionellen, freiheitliebenden Bürger und jeden Spaziergänger, ich kann es ausdrücklich empfehlen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 764

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