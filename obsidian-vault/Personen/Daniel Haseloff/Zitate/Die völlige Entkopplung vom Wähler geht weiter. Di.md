---
type: zitat
speaker: "[[Daniel Haseloff]]"
date: 2024-09-06
topic: Demokratieprinzip
page_bfv: 569
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Daniel Haseloff]] vom 6.9.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die völlige Entkopplung vom Wähler geht weiter. Die Blase der Scheindemokratie des Parteienkartells muss deutlicher zum Platzen gebracht werden. #Brandenburgwahl2024 kann der nächste nötige Nadelstich sein.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 569

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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