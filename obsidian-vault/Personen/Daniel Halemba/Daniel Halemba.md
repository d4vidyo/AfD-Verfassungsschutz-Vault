---
type: person
name: Daniel Halemba
gender: male
state: Bayern
is_still_member: true
id: 039
relevance: 5
---

# Zur Person Daniel Halemba
> [!info] 
>Landtagsabgeordneter in Bayern (seit Oktober 2023), Landesvorstandsmitglied der Jungen Alternative Bayern (Januar 2021 bis Januar 2023), Kreisvorstand Würzburg(seit 2023), Bezirksvorstand Unterfranken(seit 2020), Parteiordnungsmaßnahmen verhängt, kein Parteiausschluss
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
