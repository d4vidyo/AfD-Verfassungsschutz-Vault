---
type: zitat
speaker: "[[Harald Weyel]]"
date: 2021-12-06
topic: Demokratieprinzip
page_bfv: 613
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Harald Weyel]] vom 6.12.2021 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ich sag doch: Das "Reich der III. Impfung" ist schon so gut wie da!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 613

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