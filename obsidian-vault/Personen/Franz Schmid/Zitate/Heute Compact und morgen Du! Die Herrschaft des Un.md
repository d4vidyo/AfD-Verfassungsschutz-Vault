---
type: zitat
speaker: "[[Franz Schmid]]"
date: 2024-07-16
topic: Sonstiges
page_bfv: 713
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Franz Schmid]] vom 16.7.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Heute Compact und morgen Du! Die Herrschaft des Unrechts wird immer aggressiver. Jetzt verbietet SPD-Bundesinnenministerin Faeser unter Beifall des gesamten Establishments das regierungskritische Magazin Compact. Das ist der schwärzeste Tag der deutschen Nachkriegsgeschichte für die Pressefreiheit. Compact ist tot – die Freiheit tot bedeutet auch Widerstand jetzt erst recht!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 713

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