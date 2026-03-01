---
type: zitat
speaker: "[[Rainer Rothfuß]]"
date: 2024-11-23
topic: Menschenwürde
page_bfv: 932
source: 'Interview'
status: Unbewertet
---

# Zitat: [[Rainer Rothfuß]] vom 23.11.2024 veröffentlicht auf: 'Interview'
> [!quote] Aussage
>Ja, das Wort Remigration wurde uns total vermiest durch eine Psy-Op, also das heißt durch psychologische Kriegsführung, konzertierte Aktionen mithilfe von Correctiv, der Bundesregierung, 1300 Organisationen, die uns angegriffen haben und den Begriff Remigration letztendlich zum Stein des Anstoßes auserkoren haben. Remigration wurde sofort gleichgesetzt mit Deportation von Millionen von Menschen. Es wurde dann angeknüpft sogar in irrsinniger Weise an die Herrschaft des Nationalsozialismus. Es wurde Deportation im Zuge von Wannsee 2.0 heraufbeschworen. Ein Irrsinn. Wirklich psychologische Kriegsführung gegen die AfD, Manipulation der Massen. [...] Und da ist es mir ganz wichtig gewesen, jetzt mal einen Punkt zu setzen hier und zu sagen, Moment, Remigration ist ein wissenschaftlicher Begriff. Dahinter steckt ein ausgeklügeltes und sogar humanes Konzept. Es ist die Wiederherstellung von Ordnung, natürliche Ordnung, Durchsetzung von Recht und Ordnung.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 932

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