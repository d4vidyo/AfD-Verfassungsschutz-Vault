---
type: person
name: Kay Gottschalk
gender: male
state: Nordrhein-Westfalen
is_still_member: true
id: 180
relevance: 4
---

# Zur Person Kay Gottschalk
> [!info] 
>Bundestagsabgeordneter für Nordrhein-Westfalen (seit September 2017), stv. Bundessprecher (Dezember 2017 bis Dezember 2019 und seit Juni 2024), stv. Vorsitzender im Landesverband Nordrhein-Westfalen (seit Februar 2022)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
