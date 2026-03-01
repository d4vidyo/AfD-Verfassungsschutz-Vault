---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2023-09-13
topic: Menschenwürde
page_bfv: 370
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 13.9.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Gestern sind auf Lampedusa 5.000 Migranten aus Afrika an einem einzigen Tag gelandet: Europa erlebt eine #Invasion. Für die Zukunft unserer Heimat brauchen wir eine #FestungEuropa und #Remigration!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 370

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