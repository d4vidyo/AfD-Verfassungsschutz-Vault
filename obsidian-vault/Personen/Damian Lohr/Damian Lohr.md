---
type: person
name: Damian Lohr
gender: male
state: Rheinland-Pfalz
is_still_member: true
id: 181
relevance: 4
---

# Zur Person Damian Lohr
> [!info] 
>Landtagsabgeordneter in Rheinland-Pfalz (seit Mai 2016), parlamentarischer Geschäftsführer der AfD-Fraktion Rheinland-Pfalz (seit 2021), JA-Bundesvorsitzender (Februar 2018 bis Februar 2021), stv. JA-Bundesvorsitzender (Januar 2014 bis November 2014), JA-Bundesvorstandsmitglied (Juni 2013 bis Januar 2014), Landesvorsitzender der Jungen Alternative Rheinland-Pfalz (August 2014 bis April 2018)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
