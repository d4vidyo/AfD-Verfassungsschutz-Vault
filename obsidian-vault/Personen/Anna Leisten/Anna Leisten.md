---
type: person
name: Anna Leisten
gender: female
state: Brandenburg
is_still_member: true
id: 073
relevance: 5
---

# Zur Person Anna Leisten
> [!info] 
>JA-Bundesvorstandsmitglied (April 2021 bis März 2025), Landesvorsitzende der Jungen Alternative Brandenburg (November 2021 bis März 2025), stv. Landesvorsitzende der Jungen Alternative Brandenburg (März 2017 bis November 2021), Landesvorstandsmitglied der Jungen Alternative Brandenburg (April 2016 bis März 2017)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
