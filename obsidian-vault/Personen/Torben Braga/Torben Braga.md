---
type: person
name: Torben Braga
gender: male
state: Thüringen
is_still_member: true
id: 097
relevance: 4
---

# Zur Person Torben Braga
> [!info] 
>Bundestagsabgeordneter für Thüringen (seit Februar 2025), Landtagsabgeordneter in Thüringen (Oktober 2019 bis März 2025), parlamentarischer Geschäftsführer der AfD-Fraktion Thüringen (seit Februar 2020), stv. Sprecher im Landesverband Thüringen (seit November 2020), Landesvorstandsmitglied Thüringen (Februar 2016 bis November 2020), Landesvorstandsmitglied der Jungen Alternative Thüringen (Oktober 2017 bis Dezember 2018), Mitarbeiter der AfD-Fraktion Thüringen (2015 bis 2019)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
