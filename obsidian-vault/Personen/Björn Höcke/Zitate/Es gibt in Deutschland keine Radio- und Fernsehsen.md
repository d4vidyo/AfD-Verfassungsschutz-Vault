---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2021-09-29
topic: Demokratieprinzip
page_bfv: 557
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 29.9.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Es gibt in Deutschland keine Radio- und Fernsehsender, die als notwendige Gegenmacht gegen die zwangsfinanzierten Staatssender auftreten könnten, um unseren Weg zu unterstützen und ihm Gehör zu verschaffen. Präsident Trump wäre ohne Fox-News nicht möglich gewesen. Ebenso wird die AfD ohne starke Medien einen Durchbruch nicht schaffen können.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 557

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