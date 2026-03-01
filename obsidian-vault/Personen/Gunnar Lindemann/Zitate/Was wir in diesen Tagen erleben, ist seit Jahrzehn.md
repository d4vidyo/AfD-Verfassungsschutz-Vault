---
type: zitat
speaker: "[[Gunnar Lindemann]]"
date: 2022-07-13
topic: Demokratieprinzip
page_bfv: 606
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gunnar Lindemann]] vom 13.7.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Was wir in diesen Tagen erleben, ist seit Jahrzehnten einmalig. Die Hilfs-Maoisten im Regierungsviertel fahren unser Land mit ihrer idiotischen Energiepolitik schneller gegen die Wand, als ihre roten Vorgänger es je vermocht hätten. [...] Wenn der feuchte Traum von sozialistischen 'Wärmehallen' wahr wird, ist das Ende des linksgrünen Regimes nur noch eine Frage von Wochen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 606

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