---
type: zitat
speaker: "[[Anton Friesen]]"
date: 2021-06-10
topic: Menschenwürde
page_bfv: 496
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Anton Friesen]] vom 10.6.2021 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>#Bundesregierung sollt die nationalen Interessen Deutschlands vertreten, anstatt #Globalisten wie #Soros mit deutschem Steuergeld zu fördern!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 496

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