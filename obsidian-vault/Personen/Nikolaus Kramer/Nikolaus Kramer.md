---
type: person
name: Nikolaus Kramer
gender: male
state: Mecklenburg-Vorpommern
is_still_member: true
id: 007
relevance: 4
---

# Zur Person Nikolaus Kramer
> [!info] 
>Landtagsabgeordneter in Mecklenburg-Vorpommern (seit September 2016), Vorsitzender der AfD-Fraktion Mecklenburg-Vorpommern (seit Oktober 2017), Landesvorstandsmitglied Mecklenburg-Vorpommern (November 2016 bis November 2023), Mitglied des Landesschiedsgerichts Mecklenburg-Vorpommern (November 2014 bis November 2015)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
