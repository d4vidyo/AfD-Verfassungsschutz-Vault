---
type: person
name: Björn Höcke
gender: male
state: Thüringen
is_still_member: true
id: 030
relevance: 2
---

# Zur Person Björn Höcke
> [!info] 
>Landtagsabgeordneter in Thüringen (seit September 2014), Vorsitzender der AfD-Fraktion Thüringen (seit September 2014), Vorsitzender im Landesverband Thüringen (seit August 2013)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
