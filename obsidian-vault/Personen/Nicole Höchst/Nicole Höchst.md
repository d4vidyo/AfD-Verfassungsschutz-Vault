---
type: person
name: Nicole Höchst
gender: female
state: Rheinland-Pfalz
is_still_member: true
id: 021
relevance: 4
---

# Zur Person Nicole Höchst
> [!info] 
>Bundestagsabgeordnete für Rheinland-Pfalz (seit September 2017), stv. Vorsitzende im Landesverband Rheinland-Pfalz (seit Mai 2022), Kuratoriumsmitglied der parteinahen Desiderius-Erasmus-Stiftung
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
