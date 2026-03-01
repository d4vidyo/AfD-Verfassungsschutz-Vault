---
type: zitat
speaker: "[[Thorsten Weiß]]"
date: 2024-07-21
topic: Menschenwürde
page_bfv: 373
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Thorsten Weiß]] vom 21.7.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ich bin mit meinen Kindern gerade auf einer bekannten Erlebnisanlage in Brandenburg. Keine Talahons und keine Kulturfremden mit Drang zur Landnahme weit und breit. Es ist trotz der vielen Kinder ruhig, friedlich und zivilisiert. Das müssen wir uns zurückholen. Überall.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 373

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