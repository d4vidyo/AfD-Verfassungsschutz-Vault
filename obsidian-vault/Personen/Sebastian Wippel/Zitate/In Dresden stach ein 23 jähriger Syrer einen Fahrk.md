---
type: zitat
speaker: "[[Sebastian Wippel]]"
date: 2022-10-31
topic: Menschenwürde
page_bfv: 317
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Sebastian Wippel]] vom 31.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>In Dresden stach ein 23 jähriger Syrer einen Fahrkartenkontrolleur der Verkehrsbetriebe nieder, sodass dieser hätte zu Tode kommen können. Was ist das für eine Einstellung? So benehmen sich keine Flüchtlinge, sondern Krieger! Dieser so genannte 'Schutzbedürftige' gehört abgeschoben und das schnellstens! Die Politik hätte schon längst Konsequenten aus der seit 2015 anhaltenden Gewalt ziehen müssen. Macht sie aber nicht, weil der edle Fremde grundsätzlich gut ist und nur wenige geistesgestörte Ausnahmen auffällig werden. Allerdings müssten selbst Menschen mit dieser naiven Einstellung langsam zu der Erkenntnis kommen, dass aus bestimmten Weltregionen offenbar überdurchschnittlich viele dieser Geisteskranken kommen, und das es besser wäre die eigene Bevölkerung diesem Risiko nicht auszusetzen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 317

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