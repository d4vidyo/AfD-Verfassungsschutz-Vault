---
type: zitat
speaker: "[[Sebastian Koch]]"
date: 2024-09-25
topic: Menschenwürde
page_bfv: 174
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Sebastian Koch]] vom 25.9.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>In Bezug auf Kriminalität und Hass gegen Frauen bleibe ich bei der Aussage – eine Geburt lässt den kulturellen Erbstrang nicht beschneiden. Das sieht man bei den ganzen Talahons die schwerst frauenfeindlich und rassistisch gegen Deutsche handeln obwohl sie in der 3. Generation hier leben. Daran ändert auch kein Stück Papier etwas.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 174

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