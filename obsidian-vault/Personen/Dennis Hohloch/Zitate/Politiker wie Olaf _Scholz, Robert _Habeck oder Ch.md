---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2023-07-20
topic: Menschenwürde
page_bfv: 325
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 20.7.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Politiker wie Olaf #Scholz, Robert #Habeck oder Christian #Lindner fördern durch ihre illegale #Massenmigration schlimmste Gewaltverbrechen. Mittlerweile sind 56% der #Straftäter von Gruppenvergewaltigungen #Ausländer. Über die Hälfte der misshandelten und missbrauchten Frauen hätte dieses Schicksal ohne jene Politiker nicht durchleben müssen. Zudem ist von einer hohen Dunkelziffe auszugehen; geschweige von den Tätern, die bereits 2014/15 illegal in unser Land kamen und mittlerweile die Staatsbürgerschaft geschenkt bekommen haben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 325

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