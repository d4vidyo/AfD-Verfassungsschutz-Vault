---
type: person
name: Martin Renner
gender: male
state: Nordrhein-Westfalen
is_still_member: true
id: 035
relevance: 4
---

# Zur Person Martin Renner
> [!info] 
>Bundestagsabgeordneter für Nordrhein-Westfalen (seit September 2017), Vorsitzender im Landesverband Nordrhein-Westfalen (August 2015 bis Dezember 2017)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
