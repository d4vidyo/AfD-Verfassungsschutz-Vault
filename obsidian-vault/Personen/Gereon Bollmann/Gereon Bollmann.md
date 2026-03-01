---
type: person
name: Gereon Bollmann
gender: male
state: Schleswig-Holstein
is_still_member: true
id: 065
relevance: 5
---

# Zur Person Gereon Bollmann
> [!info] 
>Bundestagsabgeordneter für Schleswig-Holstein (seit September 2017), Präsident des Bundesschiedsgerichts (Juni 2022 bis Juni 2024), Vorsitzender des Landesschiedsgerichts Schleswig-Holstein (2017 bis 2022), Mitglied der Landesprogrammkommission (seit mindestens 2021)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
