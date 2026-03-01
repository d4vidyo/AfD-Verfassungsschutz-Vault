---
type: zitat
speaker: "[[Alexander Claus]]"
date: 2024-01-20
topic: Menschenwürde
page_bfv: 249
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Alexander Claus]] vom 20.1.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Für die Väter des GG war es eine Selbstverständlichkeit, dass die BRD ein Staat der Deutschen sein soll. Verfassungsfeinde sind die, die das GG ohne Volksabstimmung uminterpretieren und aus Deutschland Multikulti-Land machen. #Staatsbürgerschaftsrecht

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 249

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