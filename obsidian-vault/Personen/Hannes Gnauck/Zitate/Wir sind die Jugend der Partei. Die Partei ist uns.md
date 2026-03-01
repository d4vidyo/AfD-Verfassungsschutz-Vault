---
type: zitat
speaker: "[[Hannes Gnauck]]"
date: 2025-01-12
topic: Sonstiges
page_bfv: 865
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hannes Gnauck]] vom 12.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir sind die Jugend der Partei. Die Partei ist unsere Mutter. Das abzulehnen, ergibt in sich keinen Sinn. Eine Autonomie von der eigenen Partei einzufordern als Grundlage ist bestenfalls eine stark abstrahierte Ansicht dessen, was und wie eine Parteijugend strukturiert sein sollte. [...]. Bringen wir gemeinsam eine in der Partei organisierte, professionelle, gut strukturierte, disziplinierte, gut finanzierte, schlagkräftige und repräsentative Jugendorganisation auf den Weg. Am Ende steht die AfD auf den Wahlzetteln und der Wahlerfolg unserer AfD zum Wohle unseres geliebten Vaterlandes ist die Maxime unseres Handelns. Deswegen bitte ich euch um eure Zustimmung.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 865

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