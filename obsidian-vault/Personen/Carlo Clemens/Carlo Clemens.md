---
type: person
name: Carlo Clemens
gender: male
state: Nordrhein-Westfalen
is_still_member: true
id: 118
relevance: 4
---

# Zur Person Carlo Clemens
> [!info] 
>Landtagsabgeordneter in Nordrhein-Westfalen (seit Juni 2022), Bundesvorstandsmitglied (Juni 2022 bis Juni 2024), JA-Bundesvorsitzender (April 2021 bis Oktober 2022), Landesvorsitzender der Jungen Alternative Nordrhein-Westfalen (Juli 2017 bis Oktober 2021)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
