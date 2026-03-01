---
type: zitat
speaker: "[[Roland Ulbrich]]"
date: 2022-10-28
topic: Menschenwürde
page_bfv: 306
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Roland Ulbrich]] vom 28.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>'Aus Hass Häuser anzuzünden, weil man Geflüchtete nicht in seiner Nähe haben möchte, ist zutiefst primitiv und menschenverachtend', ereiferte sich Schuster weiter - ganz im Duktus der Gutmenschen-Gesellschaft, die sogar bestialische Macheten-Killer zum schuldunfähigen 'Schutzsuchenden' verklärt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 306

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