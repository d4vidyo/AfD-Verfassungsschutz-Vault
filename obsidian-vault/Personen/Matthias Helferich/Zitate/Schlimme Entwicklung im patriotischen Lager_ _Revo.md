---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2023-12-19
topic: Sonstiges
page_bfv: 780
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 19.12.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Schlimme Entwicklung im patriotischen Lager: #RevolteRheinland wird auf UVL gesetzt und zwei nette #Homos kriegen Druck bei der @AlternativeNRW, weil sie Jesiden abschieben wollen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 780

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