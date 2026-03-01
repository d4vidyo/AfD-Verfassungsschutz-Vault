---
type: person
name: Matthias Helferich
gender: male
state: Nordrhein-Westfalen
is_still_member: true
id: 053
relevance: 4
---

# Zur Person Matthias Helferich
> [!info] 
>Bundestagsabgeordneter für Nordrhein-Westfalen (September 2021 bis Februar 2025 fraktionslos, ab Februar 2025 als AfD-Fraktionsmitglied), Landesvorstandsmitglied Nordrhein-Westfalen (Februar 2024 bis Juni 2024), laufendes Parteiausschlussverfahren
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
