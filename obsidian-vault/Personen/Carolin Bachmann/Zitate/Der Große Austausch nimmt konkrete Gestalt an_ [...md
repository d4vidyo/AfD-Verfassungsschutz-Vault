---
type: zitat
speaker: "[[Carolin Bachmann]]"
date: 2022-10-11
topic: Sonstiges
page_bfv: 725
source: 'COMPACT'
status: Unbewertet
---

# Zitat: [[Carolin Bachmann]] vom 11.10.2022 veröffentlicht auf: 'COMPACT'
> [!quote] Aussage
>Der Große Austausch nimmt konkrete Gestalt an: [...] Gegenwärtig leben in Deutschland laut Statistischem Bundesamt beinahe 12 Millionen Ausländer. Dazu kommen gute 22 Millionen Menschen mit Migrationshintergrund. Die Deutschen hingegen werden jedes Jahr weniger. Aktuell leben in Deutschland – diese Angabe stammt wieder vom Statistischen Bundesamt – knapp 60 Millionen Deutsche.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 725

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