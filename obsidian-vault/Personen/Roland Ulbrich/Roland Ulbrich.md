---
type: person
name: Roland Ulbrich
gender: male
state: Sachsen
is_still_member: true
id: 023
relevance: 5
---

# Zur Person Roland Ulbrich
> [!info] 
>Landtagsabgeordneter in Sachsen (September 2019 bis September 2024), Mitglied des Bundesschiedsgerichts (Juni 2022 bis Januar 2024), Fraktionsaustritt Januar 2024, Parteiausschlussverfahren angekündigt
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
