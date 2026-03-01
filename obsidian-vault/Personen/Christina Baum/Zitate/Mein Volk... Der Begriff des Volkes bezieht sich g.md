---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-08-21
topic: Menschenwürde
page_bfv: 490
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 21.8.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Mein Volk... Der Begriff des Volkes bezieht sich ganz eindeutig auf eine Abstammungsgemeinschaft - auf eine ethnisch gleiche Gruppe. In Deutschland wird jeder zum Rassisten erklärt, der sich für den Erhalt des eigenen deutschen Volkes als ethnische Einheit einsetzt. Denn das Ziel der weltweit agierenden finanzstarken, selbsternannten ,Eliten' ist die Zerstörung dieser stabilen Strukturen innerhalb eines jeden Volkes, um die bindungs- und identitätslosen Menschen leichter manipulieren und lenken zu können. [...] Und wenn ich deshalb als Rassist beschimpft werde, weiß ich es richtig einzuordnen. Von den Vasallen der Deutschlandzerstörer so genannt zu werden, ist eher eine Auszeichnung.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 490

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