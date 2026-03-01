---
type: zitat
speaker: "[[Siegbert Droese]]"
date: 2023-09-18
topic: Demokratieprinzip
page_bfv: 586
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Siegbert Droese]] vom 18.9.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ist Roderich Kiesewetter (CDU) ein Nazi? Der hatte gestern bei #AnneWill einen denkwürdigen Auftritt. Soviel widerlichen Russenhass hat man in D wahrscheinlich das letzte mal unter Himmlers Rassenkriegern erlebt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 586

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