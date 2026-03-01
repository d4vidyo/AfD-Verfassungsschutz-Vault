---
type: zitat
speaker: "[[René Springer]]"
date: 2024-08-03
topic: Menschenwürde
page_bfv: 419
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 3.8.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Remigration oder Bürgerkrieg auf Raten. Das sind die einzigen zwei Optionen, für England wie für uns. Deshalb: Mut zu Deutschland, Mut zur millionenfachen Remigration!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 419

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