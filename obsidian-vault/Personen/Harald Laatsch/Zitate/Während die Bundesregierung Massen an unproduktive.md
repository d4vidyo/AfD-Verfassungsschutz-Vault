---
type: zitat
speaker: "[[Harald Laatsch]]"
date: 2022-09-30
topic: Menschenwürde
page_bfv: 206
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Harald Laatsch]] vom 30.9.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Während die Bundesregierung Massen an unproduktiven Migranten ins Land schleust, betreibt der assimilierte Staatsfunk Propaganda gegen Überbevölkerung, durch ethnisch Einheimische. So kommt es kontinuierlich zum Austausch.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 206

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