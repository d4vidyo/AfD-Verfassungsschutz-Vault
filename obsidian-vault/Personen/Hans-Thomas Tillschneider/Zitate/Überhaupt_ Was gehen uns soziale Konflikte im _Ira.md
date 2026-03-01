---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2022-09-29
topic: Demokratieprinzip
page_bfv: 553
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 29.9.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Überhaupt: Was gehen uns soziale Konflikte im #Iran an? Anstatt uns in die inneren Angelegenheiten souveräner Staaten einzumischen, sollten wir besser dafür sorgen, selbst #souverän zu werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 553

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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