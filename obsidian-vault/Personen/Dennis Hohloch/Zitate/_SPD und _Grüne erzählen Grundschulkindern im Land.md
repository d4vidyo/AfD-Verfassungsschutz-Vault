---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2021-07-31
topic: Menschenwürde
page_bfv: 295
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 31.7.2021 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>#SPD und #Grüne erzählen Grundschulkindern im Landtag, wie 'toll‘ und 'schön' #Massenmigration ist und dass es so wichtig ist, 'tolerant‘ und 'bunt‘ zu sein. Ich werde immer dagegen halten. Nichts ist bunt und schön an Messermännern, Islamisierung, Vergewaltigungen und Bürgergeldbetrügern.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 295

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