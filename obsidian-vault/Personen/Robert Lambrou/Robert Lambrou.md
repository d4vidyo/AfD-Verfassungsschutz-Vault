---
type: person
name: Robert Lambrou
gender: male
state: Hessen
is_still_member: true
id: 185
relevance: 4
---

# Zur Person Robert Lambrou
> [!info] 
>Landtagsabgeordneter in Hessen (seit Januar 2019), Vorsitzender der AfD-Fraktion Hessen (seit Januar 2019), Landessprecher im Landesverband Hessen (seit Januar 2019), Vorsitzender im Verein Mit Migrationshintergrund für Deutschland (seit Juni 2023)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
