---
type: person
name: Jan Nolte
gender: male
state: Hessen
is_still_member: true
id: 042
relevance: 4
---

# Zur Person Jan Nolte
> [!info] 
>Bundestagsabgeordneter für Hessen (seit September 2017), Landesvorstandsmitglied Hessen (seit November 2021), JA-Bundesvorstandsmitglied (Juli 2016 bis Februar 2018), Landesvorsitzender der Jungen Alternative Hessen (spätestens ab August 2016 bis spätestens Januar 2019)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
