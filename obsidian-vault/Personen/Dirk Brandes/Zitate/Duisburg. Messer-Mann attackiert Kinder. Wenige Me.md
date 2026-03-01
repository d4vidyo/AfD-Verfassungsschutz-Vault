---
type: zitat
speaker: "[[Dirk Brandes]]"
date: 2024-02-29
topic: Menschenwürde
page_bfv: 304
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Dirk Brandes]] vom 29.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Duisburg. Messer-Mann attackiert Kinder. Wenige Meter weiter wird 'gegen Rechts' demonstriert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 304

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