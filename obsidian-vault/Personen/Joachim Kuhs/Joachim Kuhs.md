---
type: person
name: Joachim Kuhs
gender: male
state: Baden-Württemberg
is_still_member: true
id: 041
relevance: 4
---

# Zur Person Joachim Kuhs
> [!info] 
>Europaabgeordneter (Mai 2019 bis Juni 2024), Bundesvorstandsmitglied (Dezember 2017 bis Juni 2022), Bundesvorsitzender der Christen in der AfD (seit Oktober 2017)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
