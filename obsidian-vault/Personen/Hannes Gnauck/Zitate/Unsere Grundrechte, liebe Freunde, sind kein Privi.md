---
type: zitat
speaker: "[[Hannes Gnauck]]"
date: 2022-02-25
topic: Demokratieprinzip
page_bfv: 612
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hannes Gnauck]] vom 25.2.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Unsere Grundrechte, liebe Freunde, sind kein Privileg, das allein der Willkür der Oligarchie aus Altparteien, Pharmalobby und Meinungsmachern unterliegt!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 612

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