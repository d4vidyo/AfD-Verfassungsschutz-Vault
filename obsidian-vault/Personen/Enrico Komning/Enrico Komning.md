---
type: person
name: Enrico Komning
gender: male
state: Mecklenburg-Vorpommern
is_still_member: true
id: 095
relevance: 3
---

# Zur Person Enrico Komning
> [!info] 
>Bundestagsabgeordneter für Mecklenburg-Vorpommern (seit September 2017), parlamentarischer Geschäftsführer der AfD-Bundestagsfraktion (seit Oktober 2019), Landtagsabgeordneter in Mecklenburg-Vorpommern (Oktober 2016 bis November 2017), Landesvorstandsmitglied Mecklenburg-Vorpommern (2015 bis November 2023), stv. Vorsitzender der AfD-Fraktion Mecklenburg-Vorpommern (Oktober 2016 bis November 2017)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
