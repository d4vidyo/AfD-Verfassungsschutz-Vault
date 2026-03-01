---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-05-28
topic: Menschenwürde
page_bfv: 233
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 28.5.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>4000 Afghanen monatlich – 48.000 im Jahr – zusätzlich zum Asylsystem, direkt eingeflogen, ausgewählt von NGOs, die nicht genannt werden. Das übertrifft jede Verschwörungstheorie. Die Grünen zerstören unser Land, planvoll, absichtlich und mit Komplizen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 233

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