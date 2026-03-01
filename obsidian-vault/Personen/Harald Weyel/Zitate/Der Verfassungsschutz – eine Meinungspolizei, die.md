---
type: zitat
speaker: "[[Harald Weyel]]"
date: 2023-05-25
topic: Sonstiges
page_bfv: 838
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Harald Weyel]] vom 25.5.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der Verfassungsschutz – eine Meinungspolizei, die es in den meisten demokratischen Staaten nicht gibt – verschärft seine Unterdrückung der Opposition in Form der Jungen Alternative. Ich nehme das zum Anlass, Fördermitglied zu werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 838

**Verfassungsschutz Kategorisierung:** Sonstiges.

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