---
type: person
name: Tino Chrupalla
gender: male
state: Sachsen
is_still_member: true
id: 100
relevance: 1
---

# Zur Person Tino Chrupalla
> [!info] 
>Bundestagsabgeordneter für Sachsen (seit September 2017), Vorsitzender der AfD-Bundestagsfraktion (seit September 2021), stv. Vorsitzender der AfD-Bundestagsfraktion (Oktober 2017 bis September 2021), Bundessprecher (seit November 2019), Mitglied der Bundesprogrammkommission
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
