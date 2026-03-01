---
type: zitat
speaker: "[[Erika Steinbach]]"
date: 2022-09-10
topic: Demokratieprinzip
page_bfv: 611
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Erika Steinbach]] vom 10.9.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Deutschland macht sich lächerlich. Das ist das kleinere Übel. Schlimmer ist die Abkehr von den Grundrechten der Menschen. Totalitarismus überrollt uns.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 611

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