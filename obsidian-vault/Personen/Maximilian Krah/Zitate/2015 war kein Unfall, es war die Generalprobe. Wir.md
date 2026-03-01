---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2022-12-04
topic: Menschenwürde
page_bfv: 190
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 4.12.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>2015 war kein Unfall, es war die Generalprobe. Wir erleben die Veränderung der ethnischen Zusammensetzung der Bevölkerung - verursacht durch politische Entscheidungen und in einer nie dagewesenen Geschwindigkeit. Die Deutschen werden ersetzt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 190

**Verfassungsschutz Kategorisierung:** Verstoß gegen die Menschenwürde.

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