---
type: person
name: Nils Hartwig
gender: male
state: Nordrhein-Westfalen
is_still_member: true
id: 004
relevance: 5
---

# Zur Person Nils Hartwig
> [!info] 
>stv. JA-Bundesvorsitzender (Oktober 2022 bis März 2025), JA-Bundesvorstandsmitglied (April 2021 bis Oktober 2022), stv. Landesvorsitzender der Jungen Alternative Nordrhein-Westfalen (Oktober 2021 bis Februar 2024 und seit Oktober 2024), Landesvorstandsmitglied der Jungen Alternative Nordrhein-Westfalen (Oktober 2020 bis Oktober 2021)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
