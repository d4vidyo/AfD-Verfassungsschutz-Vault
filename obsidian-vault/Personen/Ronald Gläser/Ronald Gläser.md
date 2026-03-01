---
type: person
name: Ronald Gläser
gender: male
state: Berlin
is_still_member: true
id: 184
relevance: 5
---

# Zur Person Ronald Gläser
> [!info] 
>Bundestagsabgeordneter für Berlin (seit Februar 2025), Abgeordneter im Berliner Abgeordnetenhaus (Oktober 2016 bis März 2025), parlamentarischer Geschäftsführer Berlin (2021 bis 2025), stv. Fraktionsvorsitzender Berlin (2016 bis 2021), stv. Landesvorsitzender der AfD Berlin (seit März 2021)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
