---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2021-07-10
topic: Menschenwürde
page_bfv: 444
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 10.7.2021 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Ich bin was religiöse Dinge angeht ein sehr toleranter Mensch. Ich halte es da wirklich mit dem Alten Fritz, der mal gesagt hat in religiösen Dingen soll jeder nach seiner Façon selig sein. Ja, der Islam ist eine Religion, die mir fremd ist. Vor allen Dingen seine frauenfeindliche Ausprägung, seine Ehrvorstellungen, die für mich nicht nachvollziehbar sind, seine aggressive Art, sich in anderen Ländern noch auszubreiten, wenn man dort Fuß gefasst hat, alles das entspricht nicht meinem Menschenbild und meinem politischen Wollen. Deswegen ist mir diese Kultur und der Islam als Religion und Kultur eher fremd. Und ja, der islamische Einfluss in Deutschland ist zu groß und er muss zurückgedrängt werden, gar keine Frage.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 444

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