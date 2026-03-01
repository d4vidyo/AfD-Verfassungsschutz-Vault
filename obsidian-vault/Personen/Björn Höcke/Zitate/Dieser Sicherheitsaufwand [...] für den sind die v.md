---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-08-31
topic: Demokratieprinzip
page_bfv: 565
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 31.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Dieser Sicherheitsaufwand [...] für den sind die verantwortlich, die dieses Land seit Jahren und Jahrzehnten regieren, die die innere Sicherheit zerfallen lassen und die als Kartellparteien uns als Oppositionspartei in einer Art attackieren, die man als diktatorisch einordnen muss, die uns zum Freiwild gemacht haben, uns medial nicht nur, sondern auch tatsächlich zum Abschuss freigegeben haben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 565

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