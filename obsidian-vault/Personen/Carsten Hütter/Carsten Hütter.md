---
type: person
name: Carsten Hütter
gender: male
state: Sachsen
is_still_member: true
id: 084
relevance: 4
---

# Zur Person Carsten Hütter
> [!info] 
>Landtagsabgeordneter in Sachsen (seit September 2014), Bundesvorstandsmitglied (seit November 2019), Mitglied des Bundeskonvents (seit mindestens Juni 2024), Landesvorstandsmitglied Sachsen (November 2013 bis Februar 2020)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
