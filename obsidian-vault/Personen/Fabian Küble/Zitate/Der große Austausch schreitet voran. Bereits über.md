---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2022-04-12
topic: Menschenwürde
page_bfv: 180
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 12.4.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der große Austausch schreitet voran. Bereits über 27% Nichtdeutsche in Deutschland und die Zahl wächst unaufhörlich. [...] Defacto ist dies eine entdeutschung Deutschlands.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 180

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