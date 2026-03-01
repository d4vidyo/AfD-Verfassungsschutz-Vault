---
type: person
name: Benjamin Nolte
gender: male
state: Bayern
is_still_member: true
id: 080
relevance: 5
---

# Zur Person Benjamin Nolte
> [!info] 
>Landtagsabgeordneter in Bayern (seit Oktober 2023), Landesvorstandsmitglied Bayern (November 2017 bis September 2019 und seit Oktober 2021), stv. JA-Bundesvorsitzender (Februar 2014 bis März 2014)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
