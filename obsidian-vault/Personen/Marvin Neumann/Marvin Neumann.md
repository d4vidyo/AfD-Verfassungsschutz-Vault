---
type: person
name: Marvin Neumann
gender: male
state: Brandenburg
is_still_member: false
id: 064
relevance: 5
---

# Zur Person Marvin Neumann
> [!info] 
>JA-Bundesvorsitzender (April 2021 bis Mai 2021), Landesvorstandsmitglied der Jungen Alternative Brandenburg (ab Juli 2020 bis mindestens Februar 2021), Mitarbeiter eines MdB (seit 2022), Mitarbeiter der AfD-Fraktion Brandenburg (Juni 2021 bis 2022), Parteiaustritt Mai 2021
>
>**_Ist die Person noch Mitglied:_ Nein**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
