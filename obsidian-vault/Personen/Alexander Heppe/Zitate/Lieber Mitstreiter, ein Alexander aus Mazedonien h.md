---
type: zitat
speaker: "[[Alexander Heppe]]"
date: 2023-08-04
topic: Menschenwürde
page_bfv: 375
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Alexander Heppe]] vom 4.8.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Lieber Mitstreiter, ein Alexander aus Mazedonien hat einst halb Asien erobert. Mit drei Alexanders, einem Maximilian und vielen tüchtigen Mitstreitern werden wir ganz Europa für die Europäer zurückerobern.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 375

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