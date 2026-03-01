---
type: zitat
speaker: "[[Hansjörg Schrade]]"
date: 2022-06-15
topic: Demokratieprinzip
page_bfv: 619
source: 'Reutlinger General-Anzeiger'
status: Unbewertet
---

# Zitat: [[Hansjörg Schrade]] vom 15.6.2022 veröffentlicht auf: 'Reutlinger General-Anzeiger'
> [!quote] Aussage
>Die deutschen Regierungschefs mit den meisten Todesopfern waren stets bis zum letzten Moment ihres Lebens überzeugt, mit ihren Taten im Recht gewesen zu sein.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 619

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