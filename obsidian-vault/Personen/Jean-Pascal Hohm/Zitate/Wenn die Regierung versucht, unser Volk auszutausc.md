---
type: zitat
speaker: "[[Jean-Pascal Hohm]]"
date: 2023-02-10
topic: Menschenwürde
page_bfv: 198
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Jean-Pascal Hohm]] vom 10.2.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wenn die Regierung versucht, unser Volk auszutauschen, muss das Volk die Regierung austauschen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 198

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