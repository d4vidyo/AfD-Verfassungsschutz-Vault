---
type: person
name: Dimitrios Kisoudis
gender: male
state: Berlin
is_still_member: true
id: 109
relevance: 5
---

# Zur Person Dimitrios Kisoudis
> [!info] 
>Grundsatzreferent des Bundessprechers (seit Februar 2022), Mitarbeiter eines MdB (November 2017 bis Februar 2022), Mitarbeiter eines MdEP (September 2016 bis Januar 2017)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
