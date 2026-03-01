---
type: person
name: Heiko Scholz
gender: male
state: Hessen
is_still_member: true
id: 193
relevance: 4
---

# Zur Person Heiko Scholz
> [!info] 
>Landtagsabgeordneter in Hessen (seit Oktober 2023), Bundesvorstandsmitglied (seit Juni 2024), stv. Vorsitzender im Landesverband Hessen (seit Oktober 2019), Landesvorstandsmitglied Hessen (Dezember 2017 bis Oktober 2019)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
