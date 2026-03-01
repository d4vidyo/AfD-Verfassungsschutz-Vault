---
type: zitat
speaker: "[[Christina Baum]]"
date: 2023
topic: Sonstiges
page_bfv: 721
source: 'COMPACT 11/2023'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 2023 veröffentlicht auf: 'COMPACT 11/2023'
> [!quote] Aussage
>Parlamentsarbeit ist wichtig, aber ohne die Straße können wir die Regierung nicht stürzen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 721

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