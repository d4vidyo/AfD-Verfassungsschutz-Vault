---
type: person
name: Joachim Paul
gender: male
state: Rheinland-Pfalz
is_still_member: true
id: 136
relevance: 4
---

# Zur Person Joachim Paul
> [!info] 
>Landtagsabgeordneter in Rheinland-Pfalz (seit Mai 2016), stv. Vorsitzender der AfD-Fraktion Rheinland-Pfalz (2016 bis 2021), Bundesvorstandsmitglied (November 2019 bis Juni 2022), stv. Vorsitzender im Landesverband Rheinland-Pfalz (Dezember 2017 bis November 2019), Landesvorstandsmitglied Rheinland-Pfalz
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
