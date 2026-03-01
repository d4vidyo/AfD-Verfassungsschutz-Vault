---
type: zitat
speaker: "[[Martin Renner]]"
date: 2023-08-19
topic: Demokratieprinzip
page_bfv: 605
source: 'PI-News'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 19.8.2023 veröffentlicht auf: 'PI-News'
> [!quote] Aussage
>Die 'große Transformation' nimmt an Fahrt auf – Aktuelle Meldungen zum alltäglichen Irrsinn erreichen einen fast stündlich – hier vornehmlich in den alternativen Medien. Diese Vorkommnisse werden in den 'klassischen' Medienkanälen allerdings entweder verschwiegen, oder mit unverschämter Penetranz als 'Erfolgsmeldungen' unserer öko-sozialistischen Politspinner zurechtgebogen oder glatt gelogen. Was hier stattfindet, ist allerdings keine 'große Transformation' hin zum Guten, so wie es die sich selbst Ordinierten – ins Amt Berufenen – Moralpropheten der neuen 'One-World-Religion' mit vermeintlich progressivem Stolz beständig predigen. Es ist vielmehr eine 'umgekehrte Metamorphose'. Wo hier aus einer hässlichen und gefräßigen Raupe eben kein hübscher, farbenfroher Schmetterling wird. Sondern genau umgekehrt, es wird aus einer freiheitlichen, rechtsstaatlichen und den Wohlstand generierenden Demokratie eben eine dunkle, die Freiheit verneinende Dystopie. Hinter der bereits die hässliche Fratze des Totalitarismus ungeduldig auf ihren Auftritt wartet. Eine Dystopie, in der Täter zu Opfern und Opfer zu Tätern gemacht werden. Eine Dystopie, in der öko-sozialistische Terroristen zu Aktivisten und freiheitlich-konservative Menschen zu Extremisten erklärt werden. Eine Dystopie, in der der Staat dem Einzelnen den Aufenthalt auf der Parkbank verbietet, während Vergewaltiger auf Bewährung laufen gelassen werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 605

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