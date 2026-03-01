---
type: person
name: Daniel Roi
gender: male
state: Sachsen-Anhalt
is_still_member: true
id: 116
relevance: 5
---

# Zur Person Daniel Roi
> [!info] 
>Landtagsabgeordneter in Sachsen-Anhalt (seit März 2016), parlamentarischer Geschäftsführer der AfD-Fraktion Sachsen-Anhalt (März 2016 bis November 2016), Landesvorstandsmitglied Sachsen-Anhalt (2013 bis 2014 und 2015 bis 2016), Ausschluss aus der Landtagsfraktion im Dezember 2024, laufendes Parteiausschlussverfahren
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
