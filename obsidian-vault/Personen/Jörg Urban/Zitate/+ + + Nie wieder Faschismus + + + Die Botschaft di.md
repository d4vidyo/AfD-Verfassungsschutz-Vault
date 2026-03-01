---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2023-05-08
topic: Demokratieprinzip
page_bfv: 649
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 8.5.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>+ + + Nie wieder Faschismus + + + Die Botschaft dieses Tages sollte lauten: Nie wieder Faschismus. Nie wieder Krieg. Stattdessen unterstützt die Bundesregierung in der Ukraine ein neofaschistisches Regime, das aus seiner Sympathie für die Nazis kaum einen Hehl macht.** Stattdessen ist in Deutschland mit den Grünen eine profaschistische Partei an der Regierung beteiligt, die davon träumt, die Menschen in totalitärer Weise ihrer Freiheit zu berauben. ** In der heutigen Ukraine werden ehemalige Nazi-Kollaborateure wie Stepan Bandera als Nationalhelden verehrt. Bandera ist u. a. für die Ermordung tausender Juden und Polen verantwortlich.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 649

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