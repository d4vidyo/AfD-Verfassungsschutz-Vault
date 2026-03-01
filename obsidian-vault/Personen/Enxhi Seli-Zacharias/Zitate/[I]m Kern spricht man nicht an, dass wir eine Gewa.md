---
type: zitat
speaker: "[[Enxhi Seli-Zacharias]]"
date: 2022-12-27
topic: Menschenwürde
page_bfv: 296
source: 'Hallo Meinung'
status: Unbewertet
---

# Zitat: [[Enxhi Seli-Zacharias]] vom 27.12.2022 veröffentlicht auf: 'Hallo Meinung'
> [!quote] Aussage
>[I]m Kern spricht man nicht an, dass wir eine Gewaltfantasie in einigen Kulturen haben, die durch das Messer [...] unterstrichen wird. Darüber reden wir nicht offen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 296

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