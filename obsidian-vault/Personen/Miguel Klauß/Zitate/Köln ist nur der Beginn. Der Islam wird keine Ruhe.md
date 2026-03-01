---
type: zitat
speaker: "[[Miguel Klauß]]"
date: 2022-10-15
topic: Menschenwürde
page_bfv: 476
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Miguel Klauß]] vom 15.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Köln ist nur der Beginn. Der Islam wird keine Ruhe geben, bis er überall Einzug erhalten hat. Dann ist es aber zu spät.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 476

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