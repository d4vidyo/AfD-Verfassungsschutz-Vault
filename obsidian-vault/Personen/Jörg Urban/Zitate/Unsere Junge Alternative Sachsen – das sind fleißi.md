---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2023-05-01
topic: Sonstiges
page_bfv: 839
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 1.5.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Unsere Junge Alternative Sachsen – das sind fleißige, fröhliche, feine junge Leute. Der Extremismus-Vorwurf der neuen Stasi-Behörde ist absurd

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 839

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