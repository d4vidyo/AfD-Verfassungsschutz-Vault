---
type: person
name: Hansjörg Schrade
gender: male
state: Baden-Württemberg
is_still_member: true
id: 074
relevance: 5
---

# Zur Person Hansjörg Schrade
> [!info] 
>Landesvorstandsmitglied Baden-Württemberg (Februar 2022 bis Februar 2023), Kommunalmandat in Reutlingen (seit Dezember 2021), Kreisvorstand des Kreisverbands Reutlingen (seit 2018)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
