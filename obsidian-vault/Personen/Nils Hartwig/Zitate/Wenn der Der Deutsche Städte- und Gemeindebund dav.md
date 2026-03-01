---
type: zitat
speaker: "[[Nils Hartwig]]"
date: 2021-03-31
topic: Menschenwürde
page_bfv: 118
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Nils Hartwig]] vom 31.3.2021 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wenn der Der Deutsche Städte- und Gemeindebund davon spricht, dass wir unsere Innenstädte nach der Pandemie nicht mehr wiedererkennen, heißt das dann, dass wir im Westen wieder Deutsche beim durch die Stadt bummeln sehen?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 118

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