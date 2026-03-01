---
type: person
name: René Aust
gender: male
state: Thüringen
is_still_member: true
id: 110
relevance: 3
---

# Zur Person René Aust
> [!info] 
>Europaabgeordneter (seit Juli 2024), EU-Delegationsleiter (seit Juni 2024), Landtagsabgeordneter in Thüringen (Oktober 2019 bis Juli 2024), stv. Sprecher im Landesverband Thüringen (seit 2023), Mitglied der Bundesprogrammkommission, stv. Landesvorsitzender der Jungen Alternative Thüringen (Oktober 2017 bis November 2020), Mitarbeiter der AfD-Fraktion Thüringen (2017 bis 2019)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
