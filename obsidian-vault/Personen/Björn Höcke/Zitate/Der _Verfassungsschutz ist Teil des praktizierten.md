---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2023-04-26
topic: Sonstiges
page_bfv: 839
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 26.4.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Der #Verfassungsschutz ist Teil des praktizierten Regierungsextremismus. Er schützt diejenigen, die Deutschland überwinden wollen und attackiert die Kräfte, die sich gegen die Zerstörung zur Wehr setzen. Der VS muss demokratisiert oder aufgelöst werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 839

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