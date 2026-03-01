---
type: zitat
speaker: "[[Gunnar Lindemann]]"
date: 2022-12-28
topic: Menschenwürde
page_bfv: 383
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gunnar Lindemann]] vom 28.12.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die linksgrünen Fanatiker im Berliner Senat haben offenbar jedes Augenmaß verloren. Mit ihren Aufnahmeexzessen zerstören sie jede Möglichkeit für ein friedliches Zusammenleben in unserer Stadt. Am Ende dieses Amoklaufes wird es nur Verlierer geben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 383

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