---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2021-12-19
topic: Demokratieprinzip
page_bfv: 610
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 19.12.2021 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und wer das sogar mit der DDR vergleicht, da muss ich sagen: Nein, das kann man nicht mal vergleichen. Es ist schlimmer heute als 1989!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 610

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