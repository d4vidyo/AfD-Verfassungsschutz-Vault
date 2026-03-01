---
type: person
name: Emil Sänze
gender: male
state: Baden-Württemberg
is_still_member: true
id: 032
relevance: 4
---

# Zur Person Emil Sänze
> [!info] 
>Landtagsabgeordneter in Baden-Württemberg (seit April 2016), Vorsitzender im Landesverband Baden-Württemberg (seit Juli 2022), Vorsitzender der AfD-Fraktion Baden-Württemberg (April 2016 bis Januar 2019), Mitglied des Bundeskonvents, Mitglied der Bundesprogrammkommission
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
