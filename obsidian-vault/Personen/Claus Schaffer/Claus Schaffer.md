---
type: person
name: Claus Schaffer
gender: male
state: Schleswig-Holstein
is_still_member: false
id: 146
relevance: 5
---

# Zur Person Claus Schaffer
> [!info] 
>Landtagsabgeordneter in Schleswig-Holstein (Mai 2017 bis Mai 2022), stv. Vorsitzender im Landesverband Schleswig-Holstein (April 2016 bis Juli 2017), wahrscheinlicher Parteiaustritt spätestens Oktober 2024
>
>**_Ist die Person noch Mitglied:_ Nein**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
