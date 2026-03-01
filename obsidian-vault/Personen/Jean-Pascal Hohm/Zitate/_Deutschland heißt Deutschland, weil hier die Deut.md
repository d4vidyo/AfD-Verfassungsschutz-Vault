---
type: zitat
speaker: "[[Jean-Pascal Hohm]]"
date: 2022-11-28
topic: Menschenwürde
page_bfv: 250
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Jean-Pascal Hohm]] vom 28.11.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>#Deutschland heißt Deutschland, weil hier die Deutschen leben. Nicht andersrum. Wer also das #Staatsvolk sukzessive durch #Einbürgerung ersetzt, verändert Deutschland nicht, sondern schafft es ab. Ohne Deutsche kein Deutschland. Widerstand ist darum Pflicht. Für Deutschland.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 250

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