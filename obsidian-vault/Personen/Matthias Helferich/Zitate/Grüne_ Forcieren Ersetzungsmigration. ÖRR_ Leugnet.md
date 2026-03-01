---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-05-03
topic: Menschenwürde
page_bfv: 210
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 3.5.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Grüne: Forcieren Ersetzungsmigration. ÖRR: Leugnet Ersetzungsmigration. VS: Verbietet Kritik an Ersetzungsmigration. Ersetzungsmigration: Findet statt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 210

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