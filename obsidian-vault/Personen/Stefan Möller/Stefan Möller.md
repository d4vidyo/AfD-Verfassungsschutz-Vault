---
type: person
name: Stefan Möller
gender: male
state: Thüringen
is_still_member: true
id: 198
relevance: 4
---

# Zur Person Stefan Möller
> [!info] 
>Bundestagsabgeordneter für Thüringen (seit Februar 2025), Landtagsabgeordneter in Thüringen (September 2014 bis März 2025), Landessprecher im Landesverband Thüringen (seit 2014)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
