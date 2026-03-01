---
type: person
name: Irmhild Boßdorf
gender: female
state: Nordrhein-Westfalen
is_still_member: true
id: 081
relevance: 4
---

# Zur Person Irmhild Boßdorf
> [!info] 
>Europaabgeordnete (seit Juni 2024), Vorstandsmitglied des Kreisverbands Rhein-Sieg (mindestens seit 2023), Mitarbeiterin zweier MdL (2017 bis 2022 sowie 2022 bis 2024)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
