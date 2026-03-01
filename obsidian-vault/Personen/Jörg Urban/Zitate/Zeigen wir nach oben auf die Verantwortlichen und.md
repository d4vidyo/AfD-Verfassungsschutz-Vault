---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2023-02-13
topic: Demokratieprinzip
page_bfv: 650
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 13.2.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Zeigen wir nach oben auf die Verantwortlichen und sagen, ihr seid Schuld am Krieg, ihr seid die Kriegstreiber.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 650

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