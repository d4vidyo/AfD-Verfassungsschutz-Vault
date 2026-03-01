---
type: person
name: Thorsten Weiß
gender: male
state: Berlin
is_still_member: true
id: 107
relevance: 4
---

# Zur Person Thorsten Weiß
> [!info] 
>Abgeordneter im Berliner Abgeordnetenhaus (seit Oktober 2016), stv. Vorsitzender der AfD-Fraktion Berlin (seit November 2021), Landesvorstandsmitglied Berlin (2016 bis 2020), Landesvorsitzender der Jungen Alternative Berlin (Dezember 2014 bis November 2017)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
