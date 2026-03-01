---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2023-05-01
topic: Menschenwürde
page_bfv: 133
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 1.5.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der Extremismus-Vorwurf der neuen Stasi-Behörde ist absurd, denn selbstverständlich gibt es ein deutsches Volk unabhängig vom Pass, genauso wie es ein französisches, ein jüdisches oder ein polnisches Volk gibt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 133

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