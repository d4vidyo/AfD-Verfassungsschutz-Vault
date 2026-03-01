---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2024-02-22
topic: Sonstiges
page_bfv: 833
source: 'Instagram'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 22.2.2024 veröffentlicht auf: 'Instagram'
> [!quote] Aussage
>Ich stehe zur Jungen Alternative, weil mich die Meinung von Faeser und Haldenwang nicht interessiert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 833

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