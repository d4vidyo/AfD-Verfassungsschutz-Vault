---
type: person
name: Julian Flak
gender: male
state: Schleswig-Holstein
is_still_member: true
id: 124
relevance: 5
---

# Zur Person Julian Flak
> [!info] 
>Bundesvorstandsmitglied (Juli 2015 bis Dezember 2017), Mitglied des Bundeskonvents (September 2015 bis Dezember 2017 und seit Juni 2023), stv. Vorsitzender im Landesverband Schleswig-Holstein (seit August 2022), Landesvorsitzender der Jungen Alternative Hamburg (August 2014 bis April 2016)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
