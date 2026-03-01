---
type: zitat
speaker: "[[Jörg Dornau]]"
date: 2021-09-06
topic: Demokratieprinzip
page_bfv: 555
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Dornau]] vom 6.9.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Das Grundgesetz der Bundesrepublik Deutschland ist keine Verfassung, weil sie dem Volk 'gegeben wurde'

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 555

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