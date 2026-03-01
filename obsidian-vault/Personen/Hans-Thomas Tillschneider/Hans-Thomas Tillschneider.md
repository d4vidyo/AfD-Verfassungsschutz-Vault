---
type: person
name: Hans-Thomas Tillschneider
gender: male
state: Sachsen-Anhalt
is_still_member: true
id: 140
relevance: 4
---

# Zur Person Hans-Thomas Tillschneider
> [!info] 
>Landtagsabgeordneter in Sachsen-Anhalt (seit März 2016), stv. Vorsitzender der AfD-Fraktion Sachsen-Anhalt (seit 2021), stv. Vorsitzender im Landesverband Sachsen-Anhalt (seit September 2020), Landesvorstandsmitglied Sachsen-Anhalt (Mai 2016 bis Juni 2018), Mitglied der Bundesprogrammkommission
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
