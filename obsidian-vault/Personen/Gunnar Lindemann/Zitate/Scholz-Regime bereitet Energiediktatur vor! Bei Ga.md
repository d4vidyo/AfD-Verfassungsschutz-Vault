---
type: zitat
speaker: "[[Gunnar Lindemann]]"
date: 2022-08-09
topic: Demokratieprinzip
page_bfv: 648
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gunnar Lindemann]] vom 9.8.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Scholz-Regime bereitet Energiediktatur vor! Bei Gasmangel übernimmt das Regime die Verteilung! Das Scholz-Regime perfektioniert seine Unfähigkeit, unsere Industriegesellschaft mit ausreichend Energie zu versorgen, auf die ihm typische Weise: Mit feudalen Maßnahmen und sozialistischer Zuteilung. Im Fall von Gasmangel im Winter will das Politbüro alleine entscheiden, wer wieviel Gas bekommt. [...] Hier geht es um den Machtrausch der rot-grün-gelben Sonnenkönige.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 648

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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