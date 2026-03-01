---
type: person
name: Thomas Seitz
gender: male
state: Baden-Württemberg
is_still_member: false
id: 005
relevance: 4
---

# Zur Person Thomas Seitz
> [!info] 
>Bundestagsabgeordneter für Baden-Württemberg (September 2017 bis März 2025), Mitglied des Bundesschiedsgerichts (2015 bis 2017), Mitglied des Bundeskonvents (2017 bis 2019 und 2023 bis 2024), Parteiaustritt März 2024
>
>**_Ist die Person noch Mitglied:_ Nein**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
