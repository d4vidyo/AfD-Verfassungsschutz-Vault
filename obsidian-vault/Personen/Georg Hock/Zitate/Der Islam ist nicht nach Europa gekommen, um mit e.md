---
type: zitat
speaker: "[[Georg Hock]]"
date: 2024-10-27
topic: Menschenwürde
page_bfv: 465
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Georg Hock]] vom 27.10.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der Islam ist nicht nach Europa gekommen, um mit euch Multi-Kulti zu feiern! Der Islam ist gekommen um zu herrschen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 465

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