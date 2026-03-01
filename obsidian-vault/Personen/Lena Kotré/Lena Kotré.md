---
type: person
name: Lena Kotré
gender: female
state: Brandenburg
is_still_member: true
id: 067
relevance: 5
---

# Zur Person Lena Kotré
> [!info] 
>Landtagsabgeordnete in Brandenburg (seit September 2019), stv. parlamentarische Geschäftsführerin und stv. Vorsitzende der AfD-Fraktion Brandenburg (seit Oktober 2019), Landesvorstandsmitglied Brandenburg (2017 bis 2022)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
