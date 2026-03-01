---
type: person
name: Martin Braukmann
gender: male
state: Sachsen
is_still_member: true
id: 148
relevance: 5
---

# Zur Person Martin Braukmann
> [!info] 
>Landtagsabgeordneter in Sachsen (seit September 2024), Präsident des Bundesschiedsgerichts (seit Juni 2024), Vizepräsident des Bundesschiedsgerichts (Januar 2024 bis Juni 2024), Mitglied des Bundesschiedsgerichts (seit November 2019), Vorsitzender des Landesschiedsgerichts Sachsen (2018 bis 2020)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
