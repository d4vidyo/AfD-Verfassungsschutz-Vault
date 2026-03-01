---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2023-04-16
topic: Demokratieprinzip
page_bfv: 553
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 16.4.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und wer mit den Grünen koaliert auf Bund- oder Landesebene, macht sich gemein mit genau diesen Kriegstreibern, denn sie sind gesteuert, und sie werden bezahlt für ihr schlechtes Tun.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 553

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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