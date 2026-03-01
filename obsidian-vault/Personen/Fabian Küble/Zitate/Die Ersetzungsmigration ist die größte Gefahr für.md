---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2024-11-14
topic: Menschenwürde
page_bfv: 896
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 14.11.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die Ersetzungsmigration ist die größte Gefahr für unser Volk. Der Wähleraustausch aber ist die größte Gefahr für die Demokratie & untergräbt ihre Legitimation. Sehr gefährlich.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 896

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