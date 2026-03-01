---
type: zitat
speaker: "[[Thomas Herrig]]"
date: 2022-06-27
topic: Menschenwürde
page_bfv: 369
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Thomas Herrig]] vom 27.6.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Es ist eine schwarzafrikanische Invasion Europas was wir in diesen Zeiten erleben . #Melilla ist nur ein Teil davon. Stabiler Grenzschutz ist Nötig zum Schutz unserer Gesellschaften.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 369

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