---
type: zitat
speaker: "[[Martin Hess]]"
date: 2022-12-13
topic: Menschenwürde
page_bfv: 333
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Martin Hess]] vom 13.12.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Das Land hat sich verändert. Drastisch. Man erkennt es kaum wieder. #Asylbewerber stechen Passanten nieder, vergewaltigen und ermorden junge Frauen und legen Innenstädte in Schutt und Asche.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 333

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