---
type: person
name: Jean-Pascal Hohm
gender: male
state: Brandenburg
is_still_member: true
id: 014
relevance: 5
---

# Zur Person Jean-Pascal Hohm
> [!info] 
>Landtagsabgeordneter in Brandenburg (seit Oktober 2024), Kreisvorstand des Kreisverbands Cottbus (seit 2021), Landesvorstandsmitglied der Jungen Alternative Brandenburg (März 2017 bis Juni 2018), Landesvorsitzender der Jungen Alternative Brandenburg (ab Juli 2014 bis April 2016)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
