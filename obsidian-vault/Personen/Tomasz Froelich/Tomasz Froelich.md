---
type: person
name: Tomasz Froelich
gender: male
state: Hamburg
is_still_member: true
id: 020
relevance: 4
---

# Zur Person Tomasz Froelich
> [!info] 
>Europaabgeordneter (seit Juni 2024), stv. JA-Bundesvorsitzender (seit Februar 2019), Landesvorsitzender der Jungen Alternative Hamburg (spätestens Juli 2019 bis August 2021), Mitarbeiter der AfD-Fraktion Baden-Württemberg (2016 bis 2019), Mitarbeiter der EU-Delegation (2019 bis Juni 2024)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
