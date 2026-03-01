---
type: zitat
speaker: "[[Nikolaus Kramer]]"
date: 2024-04-15
topic: Menschenwürde
page_bfv: 121
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Nikolaus Kramer]] vom 15.4.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir lieben das Eigene und wissen den Wert um die Gemeinschaft. Wir haben Wurzeln geschlagen. Wir wissen, wer wir sind, ohne dabei ein losgelöstes Individuum, ohne Bindung zu sein. Wir stehen ein für die Familie und sind Teil einer sichtbaren Ahnenkette. Für uns ist Deutschland nicht nur ein Ort, sondern Heimat, mit der wir kulturell und historisch verbunden sind.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 121

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