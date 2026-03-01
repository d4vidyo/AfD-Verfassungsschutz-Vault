---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-08-21
topic: Menschenwürde
page_bfv: 368
source: 'AUF1'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 21.8.2024 veröffentlicht auf: 'AUF1'
> [!quote] Aussage
>Was uns, glaube ich, auch fundamental unterscheidet von allen anderen Parteien - Altparteien - ist, dass wir eben ein klares Bewusstsein dafür haben, dass wir unser Land verdanken und unsere Entwicklung verdanken den Mühen und der Arbeit unserer Vorfahren. Und dass daraus auch resultiert eine Verpflichtung, dass Deutschland, dass Brandenburg, dass Thüringen, dass Sachsen auch für die kommenden Generationen eine Heimat sind. Dass sie sich nicht unterwerfen müssen, irgendwelchen Zuwanderern, sondern hier nach unserer Art leben können, dass sie hier ihre Heimat haben. Das ist eine Verpflichtung, die wir alle haben, aufgrund - wegen der vielen Mühen unserer Vorfahren, die unser Land immer wieder aus den Trümmern aufgebaut haben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 368

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