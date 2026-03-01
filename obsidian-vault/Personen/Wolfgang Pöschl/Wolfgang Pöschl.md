---
type: person
name: Wolfgang Pöschl
gender: male
state: Bayern
is_still_member: false
id: 141
relevance: 5
---

# Zur Person Wolfgang Pöschl
> [!info] 
>Kommunalmandat in Cham, Kreisvorstand des Kreisverbands Cham, Parteiausschluss Januar 2025
>
>**_Ist die Person noch Mitglied:_ Nein**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
