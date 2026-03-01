---
type: person
name: Beatrix von Storch
gender: female
state: Berlin
is_still_member: true
id: 086
relevance: 2
---

# Zur Person Beatrix von Storch
> [!info] 
>Bundestagsabgeordnete für Berlin (seit September 2017), stv. Vorsitzende der AfD-Bundestagsfraktion (seit Oktober 2017), Europaabgeordnete (Mai 2014 bis November 2017), stv. Bundessprecherin (Juli 2015 bis Dezember 2017 und Dezember 2019 bis Juni 2022), Bundesvorstandsmitglied (Dezember 2017 bis Dezember 2019), Vorsitzende im Landesverband Berlin (Januar 2016 bis November 2017)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
