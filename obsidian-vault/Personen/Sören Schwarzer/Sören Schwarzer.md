---
type: person
name: Sören Schwarzer
gender: male
state: Sachsen
is_still_member: true
id: 114
relevance: 5
---

# Zur Person Sören Schwarzer
> [!info] 
>JA-Bundesvorstandsmitglied (April 2021 bis Oktober 2022), Landesvorstandsmitglied der Jungen Alternative Sachsen (Januar 2019 bis Dezember 2019), stv. Landesvorsitzender der Jungen Alternative Sachsen (Dezember 2019 bis April 2022)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
