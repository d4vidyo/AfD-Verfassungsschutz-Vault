---
type: person
name: Sven Tritschler
gender: male
state: Nordrhein-Westfalen
is_still_member: true
id: 152
relevance: 4
---

# Zur Person Sven Tritschler
> [!info] 
>Landtagsabgeordneter in Nordrhein-Westfalen (seit Mai 2017), stv. Sprecher im Landesverband Nordrhein-Westfalen (Februar 2022 bis Februar 2024 und seit März 2025), Landesvorstandsmitglied Nordrhein-Westfalen (2014 bis 2015), JA-Bundesvorsitzender (Mai 2015 bis Februar 2018), Landesvorsitzender der Jungen Alternative Nordrhein-Westfalen (Februar 2014 bis Juli 2017)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
