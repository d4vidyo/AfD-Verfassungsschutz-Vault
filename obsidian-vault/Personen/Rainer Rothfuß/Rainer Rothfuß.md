---
type: person
name: Rainer Rothfuß
gender: male
state: Bayern
is_still_member: true
id: 155
relevance: 4
---

# Zur Person Rainer Rothfuß
> [!info] 
>Bundestagsabgeordneter für Bayern (seit März 2023), stv. Vorsitzender im Landesverband Bayern (seit Oktober 2021), Kuratoriumsmitglied der parteinahen Desiderius-Erasmus-Stiftung (seit 2018), Kommunalmandat in Lindau (seit 2020)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
