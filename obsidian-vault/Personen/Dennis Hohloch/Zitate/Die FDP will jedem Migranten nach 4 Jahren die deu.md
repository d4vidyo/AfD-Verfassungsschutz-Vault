---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2021-04-15
topic: Menschenwürde
page_bfv: 238
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 15.4.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die FDP will jedem Migranten nach 4 Jahren die deutsche #Staatsbürgerschaft ermöglichen. Diese Art des Liberalismus steht für die Selbstauflösung unserer Nation und die Abschaffung des Rechtsstaats. Das ist mit freiheitlicher #AfD-Politik unvereinbar.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 238

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