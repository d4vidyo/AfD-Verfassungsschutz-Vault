---
type: zitat
speaker: "[[Carolin Bachmann]]"
date: 2023-04-14
topic: Menschenwürde
page_bfv: 379
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Carolin Bachmann]] vom 14.4.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Anti-Deutschland-Ampel mit ihrem Sozial-Paradies Deutschland zerschmettert uns Geheimdienste warnen -\> Terroristen reisen als Asylbewerber nach Deutschland ein! Asyl-Tsunami: Italien ruft Ausnahmezustand aus!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 379

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