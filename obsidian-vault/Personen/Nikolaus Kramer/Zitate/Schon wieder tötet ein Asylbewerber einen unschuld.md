---
type: zitat
speaker: "[[Nikolaus Kramer]]"
date: 2022-12-06
topic: Menschenwürde
page_bfv: 301
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Nikolaus Kramer]] vom 6.12.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Schon wieder tötet ein Asylbewerber einen unschuldigen Menschen, ein 14-jähriges Mädchen, das nur zur Schule gehen wollte. [...] Statt harter, konsequenter Bestrafung und Abschiebung erörtern unsere Innenexperten im Bund ein Gesetz zur einfacheren Einbürgerung, welches es Messermännern noch leichter macht, schwere Straftaten auf deutschem Boden zu verüben. Schämen Sie sich dafür!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 301

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