---
type: zitat
speaker: "[[Dirk Spaniel]]"
date: 2023-10-09
topic: Menschenwürde
page_bfv: 361
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Dirk Spaniel]] vom 9.10.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Keine Sorge liebe deutsche Mitbürger, weitere Hunderte von antisemitischen Sozialbetrügern sind dank der Ampel auf dem Weg nach #Deutschland... Das ändert sich erst, wenn die #AfD eine #Regierung stellen kann. Dazu braucht sie qualifizierte Mehrheiten!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 361

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