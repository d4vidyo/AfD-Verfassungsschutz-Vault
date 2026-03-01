---
type: zitat
speaker: "[[Anton Friesen]]"
date: 2021-06-07
topic: Menschenwürde
page_bfv: 496
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Anton Friesen]] vom 7.6.2021 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die Bundesregierung fördert die Open Society Foundations von #Soros mit 200.000-300.000 Euro deutsches Steuergeld pro Jahr, wie meine Anfrage aufdeckte! #Merkel unterstützt globalistische Regime Change Pläne des Oligarchen Soros!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 496

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