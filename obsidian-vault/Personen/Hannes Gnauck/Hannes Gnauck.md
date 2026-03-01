---
type: person
name: Hannes Gnauck
gender: male
state: Brandenburg
is_still_member: true
id: 008
relevance: 3
---

# Zur Person Hannes Gnauck
> [!info] 
>Bundestagsabgeordneter für Brandenburg (seit September 2021), Bundesvorstandsmitglied (seit Juni 2024), JA-Bundesvorsitzender (Oktober 2022 bis März 2025), stv. Landesvorsitzender der Jungen Alternative Brandenburg (November 2021 bis November 2023), Landesvorstandsmitglied der Jungen Alternative Brandenburg (Januar 2020 bis November 2021)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
