---
type: zitat
speaker: "[[Jean-Pascal Hohm]]"
date: 2023-11-01
topic: Menschenwürde
page_bfv: 203
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jean-Pascal Hohm]] vom 1.11.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der Bevölkerungsaustausch ist kein 'rechtsradikales Narrativ', sondern bittere Realität. Das sieht jeder, der mit offenen Augen durch unsere Stadt geht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 203

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