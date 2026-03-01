---
type: zitat
speaker: "[[Rene Dierkes]]"
date: 2024-09-24
topic: Demokratieprinzip
page_bfv: 570
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Rene Dierkes]] vom 24.9.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Altparteienkartell entlarvt sich als Einheitspartei

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 570

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