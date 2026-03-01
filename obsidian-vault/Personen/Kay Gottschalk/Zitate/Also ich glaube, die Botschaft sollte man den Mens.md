---
type: zitat
speaker: "[[Kay Gottschalk]]"
date: 2025-01-25
topic: Menschenwürde
page_bfv: 911
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Kay Gottschalk]] vom 25.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Also ich glaube, die Botschaft sollte man den Menschen auch mittragen, wenn ihr wirklich wollt, dass eure Kinder wieder sicher zur Schule gehen, wenn ihr wollt, dass eure Töchter am Freitag auch sicher von der Diskothek nach Hause kommen, und wenn ihr wollt, dass einfach im Park eure Kinder nicht von irgendwelchen, meistens - ich weiß auch gar nicht, ob nur psychisch Gestörte nach Deutschland ein wandern. Deutschland muss das Land sein, in dem die meisten psychisch Gestörten sind.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 911

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