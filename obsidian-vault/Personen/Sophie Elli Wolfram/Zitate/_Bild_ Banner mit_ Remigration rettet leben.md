---
type: zitat
speaker: "[[Sophie Elli Wolfram]]"
date: 2025-02-26
topic: Menschenwürde
page_bfv: 930
source: 'Insta'
status: Unbewertet
---

# Zitat: [[Sophie Elli Wolfram]] vom 26.2.2025 veröffentlicht auf: 'Insta'
> [!quote] Aussage
>\<Bild\> Banner mit: Remigration rettet leben

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 930

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