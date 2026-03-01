---
type: person
name: Sven Kachelmann
gender: male
state: Bayern
is_still_member: true
id: 173
relevance: 5
---

# Zur Person Sven Kachelmann
> [!info] 
>stv. JA-Bundesvorsitzender (April 2021 bis März 2025), JA-Bundesvorstandsmitglied (Februar 2019 bis April 2021), Landesvorsitzender der Jungen Alternative Bayern (November 2017 bis Januar 2023), stv. Landesvorsitzender der Jungen Alternative Bayern (Juli 2016 bis November 2017), Landesvorstandsmitglied der Jungen Alternative Bayern (November 2015 bis Juli 2016)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
