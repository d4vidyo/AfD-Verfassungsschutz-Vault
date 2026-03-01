---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-11-17
topic: Demokratieprinzip
page_bfv: 952
source: 'X (ehemals Twitter), Repost'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 17.11.2024 veröffentlicht auf: 'X (ehemals Twitter), Repost'
> [!quote] Aussage
>Fakt ist aber auch, daß die BILD und die Kartellparteien seit vielen Jahren für die sog. 'Energiewende' trommeln, deren Rückgrat die Windenergie sein soll. Die BILD wird immer noch gelesen, die Kartellparteien mehrheitlich gewählt... #Demokratie funktioniert nicht mit Stimmungsmache, sondern nur mit gut informierten, nicht manipulierbaren und weitsichtigen Bürgern.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 952

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