---
type: person
name: Sebastian Münzenmaier
gender: male
state: Rheinland-Pfalz
is_still_member: true
id: 071
relevance: 3
---

# Zur Person Sebastian Münzenmaier
> [!info] 
>Bundestagsabgeordneter für Rheinland-Pfalz (seit September 2017), stv. Vorsitzender der AfD-Bundestagsfraktion (seit 2019), stv. Vorsitzender im Landesverband Rheinland-Pfalz (seit 2017), Mitarbeiter der AfD-Fraktion Rheinland-Pfalz (2016 bis Oktober 2017), Landesvorsitzender der Jungen Alternative Rheinland-Pfalz (spätestens August 2013 bis spätestens August 2014)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
