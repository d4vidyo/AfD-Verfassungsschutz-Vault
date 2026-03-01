---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-08-31
topic: Demokratieprinzip
page_bfv: 567
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 31.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Liebe Freunde, der 1. September 2024 kann eine historische Zäsur bedeuten. Er kann dazu führen, dass das Kartellparteiensystem der Bundesrepublik Deutschland implodiert und dass endlich etwas entsteht, was eine wirkliche Demokratie ist.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 567

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