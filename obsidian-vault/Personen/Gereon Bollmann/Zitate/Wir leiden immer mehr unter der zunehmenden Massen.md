---
type: zitat
speaker: "[[Gereon Bollmann]]"
date: 2024-12-22
topic: Menschenwürde
page_bfv: 889
source: 'gereon-bollmann.de'
status: Unbewertet
---

# Zitat: [[Gereon Bollmann]] vom 22.12.2024 veröffentlicht auf: 'gereon-bollmann.de'
> [!quote] Aussage
>Wir leiden immer mehr unter der zunehmenden Massenmigration, hinter der sich der geplante Austausch unseres Volkes verbirgt. Heimlich still und leise läuft das internationale Programm der Globalisten ohne Unterbrechung weiter. Dies ist eben keine Verschwörungstheorie, sondern in den entsprechenden Planungen unserer Gegner (compact for migration, resettlement migration, WEF, usw.) fest verankert. Wir werden von Jahr zu Jahr immer weniger, und niemand regt sich auf.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 889

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