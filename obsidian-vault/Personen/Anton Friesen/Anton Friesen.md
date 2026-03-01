---
type: person
name: Anton Friesen
gender: male
state: Thüringen
is_still_member: true
id: 138
relevance: 4
---

# Zur Person Anton Friesen
> [!info] 
>Bundestagsabgeordneter für Thüringen (September 2017 bis September 2021), Landesvorsitzender der Jungen Alternative Thüringen (2017 bis 2019), Landesvorstandsmitglied der Jungen Alternative Thüringen (2016 bis 2017), Fraktionsreferent Thüringen (2015 bis 2017)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
