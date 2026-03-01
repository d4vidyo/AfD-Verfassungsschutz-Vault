---
type: zitat
speaker: "[[René Aust]]"
date: 2022-12-05
topic: Menschenwürde
page_bfv: 355
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[René Aust]] vom 5.12.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Höhere Diversität ist mit erheblich mehr Konflikten verbunden. Diese Konflikte werden häufiger mit Gewalt ausgetragen. 'Weltoffene'/Bunte Gesellschaften sind schwach, ungleich und gewalttätig.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 355

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