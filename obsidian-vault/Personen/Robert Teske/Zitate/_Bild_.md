---
type: zitat
speaker: "[[Robert Teske]]"
date: 2023-09-17
topic: Menschenwürde
page_bfv: 400
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Robert Teske]] vom 17.9.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>\<Bild\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 400. Post eines Comics

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