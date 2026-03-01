---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2024-08-01
topic: Sonstiges
page_bfv: 715
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 1.8.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ich freue mich, mit dem ehemaligen Compact-Chefredakteur Jürgen Elsässer eine starke Stimme für die Pressefreiheit auf unserem Parteitag am 17./18. August in Magdeburg begrüßen zu dürfen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 715

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