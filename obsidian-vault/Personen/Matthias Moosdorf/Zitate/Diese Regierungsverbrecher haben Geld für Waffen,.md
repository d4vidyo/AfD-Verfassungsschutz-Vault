---
type: zitat
speaker: "[[Matthias Moosdorf]]"
date: 2024-02-02
topic: Demokratieprinzip
page_bfv: 640
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Moosdorf]] vom 2.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Diese Regierungsverbrecher haben Geld für Waffen, Munition und Korruption in der Ukraine. Selbst die Neubauprojekte der Deutschen Bahn, einer im Investitionsstau steckenden Lebensader dieses Landes und seiner Wirtschaft, werden dafür geopfert. Macht Euch selbst ein Bild und wählt diese machtgeile Clique von Deutschland-Hassern ab. Dieses Jahr ist dazu reichlich Gekegenheit.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 640

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