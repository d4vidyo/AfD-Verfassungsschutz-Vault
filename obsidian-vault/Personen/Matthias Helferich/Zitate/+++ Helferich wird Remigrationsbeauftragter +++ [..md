---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2022-10-13
topic: Menschenwürde
page_bfv: 414
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 13.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>+++ Helferich wird Remigrationsbeauftragter +++ [...] Es scheint, als habe die Union vergessen, wer 2015/2016 die Grenzen offen ließ und Deutschland der Massenmigration schutzlos auslieferte.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 414

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