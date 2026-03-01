---
type: zitat
speaker: "[[Tomasz Froelich]]"
date: 2021-12-25
topic: Menschenwürde
page_bfv: 195
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Tomasz Froelich]] vom 25.12.2021 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Statistiken zur Demographie machen deutlich: Ein Bevölkerungsaustausch findet statt. Das ist Fakt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 195

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