---
type: person
name: Christian Blex
gender: male
state: Nordrhein-Westfalen
is_still_member: true
id: 190
relevance: 4
---

# Zur Person Christian Blex
> [!info] 
>Landtagsabgeordneter in Nordrhein-Westfalen (seit Juni 2017), Landesvorstandsmitglied Nordrhein-Westfalen (seit Februar 2022), Mitglied der AfD-Fraktion im Landtag Nordrhein-Westfalen (Juni 2017 bis September 2022, seit Januar 2024)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
