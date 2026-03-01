---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2023-12-24
topic: Sonstiges
page_bfv: 778
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 24.12.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Frohe Weihnachten auch an die mutigen Aktivisten der Gruppe 'Revolte Rheinland'! Möge Eure kraftvolle Botschaft des Friedens und der Liebe auch im Jahr 2024 im ganzen Deutschland gehört werden. [...] Die Revolution frisst ihre eigenen Kinder? Möge es bei uns anders laufen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 778

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