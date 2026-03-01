---
type: person
name: Alice Weidel
gender: female
state: Baden-Württemberg
is_still_member: true
id: 044
relevance: 1
---

# Zur Person Alice Weidel
> [!info] 
>Bundestagsabgeordnete für Baden-Württemberg (seit September 2017), Vorsitzende der AfD-Bundestagsfraktion (seit September 2017), Bundessprecherin (seit Juni 2022), Vorsitzende im Landesverband Baden-Württemberg (Februar 2020 bis Juli 2022)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
