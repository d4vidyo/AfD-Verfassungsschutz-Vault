---
type: zitat
speaker: "[[René Springer]]"
date: 2023-06-14
topic: Menschenwürde
page_bfv: 281
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 14.6.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Das effektivste Mittel gegen gewalttätige Übergriffe in Zügen ist kein #Messer-Verbot, sondern #Remigration!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 281

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