---
type: zitat
speaker: "[[Enrico Schult]]"
date: 2023-04-28
topic: Sonstiges
page_bfv: 838
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Enrico Schult]] vom 28.4.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ich stelle mich als Landessprecher demonstrativ hinter unsere Junge Alternative Mecklenburg-Vorpommern und habe heute sogleich eine Fördermitgliedschaft abgeschlossen

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