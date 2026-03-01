---
type: person
name: Stephan Brandner
gender: male
state: Thüringen
is_still_member: true
id: 055
relevance: 2
---

# Zur Person Stephan Brandner
> [!info] 
>Bundestagsabgeordneter für Thüringen (seit September 2017), zweiter parlamentarischer Geschäftsführer der AfD-Bundestagsfraktion (seit September 2021), stv. Bundessprecher (seit Dezember 2019), Landtagsabgeordneter in Thüringen (Oktober 2014 bis Oktober 2017)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
