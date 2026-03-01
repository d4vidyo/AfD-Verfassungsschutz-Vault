---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-09-08
topic: Demokratieprinzip
page_bfv: 625
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 8.9.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Was sind das für Richter, die heutzutage, da islamischer Terror bereits in Deutschland stattfindet und sich deutsche Gerichte mit der Zwangsverheiratung von Kindern beschäftigen müssen, jegliche kritische Meinungsäußerung zu diesen Themen bestrafen? Man könnte fast annehmen, daß hier jemand vor den demographischen Realitäten der Verdrängungs-/Masseneinwanderung innerlich kapituliert hat und die Fortführung seiner Karriere im künftigen Kalifat auf deutschem Boden nicht gefährden will... Auch wenn Michael Stürzenberger, wie so viele Dissidenten, den Glauben an den Rechtsstaat längst verloren haben dürfte, geht er in die nächste Instanz. Ich wünsche dem leidenschaftlichen Aufklärer, daß ihn die Kraft nicht verläßt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 625

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