---
type: person
name: Florian Jäger
gender: male
state: Bayern
is_still_member: false
id: 142
relevance: 5
---

# Zur Person Florian Jäger
> [!info] 
>Bundestagsabgeordneter für Bayern (Juli 2021 bis September 2021), Mitglied des Bundeskonvents (2019 bis 2024), Mitarbeiter eines MdB (2017 bis 2021), Parteiaustritt Juli 2024
>
>**_Ist die Person noch Mitglied:_ Nein**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
