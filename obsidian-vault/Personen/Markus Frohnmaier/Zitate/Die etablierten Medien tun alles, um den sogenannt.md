---
type: zitat
speaker: "[[Markus Frohnmaier]]"
date: 2025-01-20
topic: Menschenwürde
page_bfv: 893
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Markus Frohnmaier]] vom 20.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die etablierten Medien tun alles, um den sogenannten ,Bevölkerungsaustausch' als rechtsextreme Verschwörungstheorie abzustempeln. Doch währenddessen verkündet SPD-Liebling Sawsan Chebli kühl:,Demographie wird Fakten schaffen'. Welche Fakten meint sie genau? Ist das eine klare Ansage - oder sogar eine Drohung?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 893

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