---
type: person
name: Alexander Jungbluth
gender: male
state: Rheinland-Pfalz
is_still_member: true
id: 131
relevance: 4
---

# Zur Person Alexander Jungbluth
> [!info] 
>Europaabgeordneter (seit Juli 2024), Bundesvorstandsmitglied (seit Juni 2024), Mitglied des Bundeskonvents (seit Juni 2024), Landesvorsitzender der Jungen Alternative Rheinland-Pfalz (April 2018 bis Juli 2021), Landesvorstandsmitglied der Jungen Alternative Rheinland-Pfalz (September 2022 bis spätestens Juli 2024), Mitarbeiter eines MdB (bis Juni 2024)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
