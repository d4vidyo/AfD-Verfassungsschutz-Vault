---
type: person
name: Reimond Hoffmann
gender: male
state: Baden-Württemberg
is_still_member: true
id: 057
relevance: 5
---

# Zur Person Reimond Hoffmann
> [!info] 
>Landesvorstandsmitglied Baden-Württemberg (Juli 2022 bis Februar 2024), stv. JA-Bundesvorsitzender (Juli 2016 bis Februar 2018), stv. Landesvorsitzender der Jungen Alternative Baden-Württemberg (September 2018 bis März 2019), laufendes Parteiausschlussverfahren
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
