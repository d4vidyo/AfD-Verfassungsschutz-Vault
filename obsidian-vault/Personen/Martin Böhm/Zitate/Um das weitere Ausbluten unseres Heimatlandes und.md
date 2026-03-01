---
type: zitat
speaker: "[[Martin Böhm]]"
date: 2024-03-05
topic: Menschenwürde
page_bfv: 414
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Böhm]] vom 5.3.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Um das weitere Ausbluten unseres Heimatlandes und die konzertierte Zerstörung der Zukunft unserer Kinder zu verhindern, gibt es nur einen Weg: REMIGRATION.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 414

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