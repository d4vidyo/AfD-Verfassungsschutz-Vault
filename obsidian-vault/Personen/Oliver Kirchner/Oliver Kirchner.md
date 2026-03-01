---
type: person
name: Oliver Kirchner
gender: male
state: Sachsen-Anhalt
is_still_member: true
id: 013
relevance: 3
---

# Zur Person Oliver Kirchner
> [!info] 
>Landtagsabgeordneter in Sachsen-Anhalt (seit März 2016), Vorsitzender der AfD-Fraktion Sachsen-Anhalt (seit März 2018), stv. Vorsitzender im Landesverband Sachsen-Anhalt (seit 2023), Landesvorstandsmitglied Sachsen-Anhalt (2021 bis 2023)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
