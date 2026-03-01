---
type: person
name: Katrin Ebner-Steiner
gender: female
state: Bayern
is_still_member: true
id: 103
relevance: 4
---

# Zur Person Katrin Ebner-Steiner
> [!info] 
>Landtagsabgeordnete in Bayern (seit Oktober 2018), Vorsitzende der AfD-Fraktion Bayern (Oktober 2018 bis September 2021 und seit Oktober 2023), stv. Vorsitzende im Landesverband Bayern (Oktober 2017 bis September 2019), Landesvorstandsmitglied Bayern (Oktober 2015 bis Oktober 2017)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
