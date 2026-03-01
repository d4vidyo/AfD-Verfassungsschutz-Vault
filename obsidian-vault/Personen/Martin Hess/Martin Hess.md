---
type: person
name: Martin Hess
gender: male
state: Baden-Württemberg
is_still_member: true
id: 104
relevance: 4
---

# Zur Person Martin Hess
> [!info] 
>Bundestagsabgeordneter für Baden-Württemberg (seit September 2017), stv. Vorsitzender im Landesverband Baden-Württemberg (März 2017 bis Februar 2019 und Februar 2020)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
