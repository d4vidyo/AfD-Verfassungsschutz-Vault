---
type: zitat
speaker: "[[Norbert Mayer]]"
date: 2024-02-01
topic: Demokratieprinzip
page_bfv: 607
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Norbert Mayer]] vom 1.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>!! Altparteien-Mafia abwählen !! Auf unserer Freitaler Kundgebung unter dem Titel 'Freiheit, Heimat Tradition.' , fand ich deutliche Worte für die Märchenstunden-Propaganda des 'Regierungs-Schutzes' gegen die AfD. [...] Deshalb heißt es am 1. September: Altparteien-Mafia abwählen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 607

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