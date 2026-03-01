---
type: zitat
speaker: "[[Stephan Brandner]]"
date: 2023-06-26
topic: Demokratieprinzip
page_bfv: 637
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Stephan Brandner]] vom 26.6.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die #Altparteien tragen die Verantwortung für die Zustände in Deutschland: Sie regieren wie ein politischer #Swingerclub. Jeder mit jedem, alles und immer. Und das seit etwa 75 Jahren!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 637

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