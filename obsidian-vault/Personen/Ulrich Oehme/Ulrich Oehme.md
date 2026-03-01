---
type: person
name: Ulrich Oehme
gender: male
state: Sachsen
is_still_member: true
id: 049
relevance: 5
---

# Zur Person Ulrich Oehme
> [!info] 
>Bundestagsabgeordneter für Sachsen (September 2017 bis September 2021), Bundesvorsitzender der Christen in der AfD (seit 2015), Landesvorstandsmitglied Sachsen (2016 bis 2017)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
