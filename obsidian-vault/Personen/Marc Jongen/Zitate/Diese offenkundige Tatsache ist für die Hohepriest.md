---
type: zitat
speaker: "[[Marc Jongen]]"
date: 2023-02-01
topic: Menschenwürde
page_bfv: 241
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Marc Jongen]] vom 1.2.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Diese offenkundige Tatsache ist für die Hohepriester der neuen Woke-Religion gerade deshalb so empörend, weil der Rassismus gegen Weiße in der politisch medialen Klasse Deutschlands zunehmend grassiert. Ausdruck davon sind die immer irrsinnigeren Formen des kulturellen Selbsthasses und der Selbstabschaffung.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 241

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