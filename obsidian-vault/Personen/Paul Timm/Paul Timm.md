---
type: person
name: Paul Timm
gender: male
state: Mecklenburg-Vorpommern
is_still_member: true
id: 026
relevance: 5
---

# Zur Person Paul Timm
> [!info] 
>Landtagsabgeordneter in Mecklenburg-Vorpommern (seit Oktober 2021), Mitglied des Landesschiedsgerichts Mecklenburg-Vorpommern (seit November 2021), Landesvorstandsmitglied der Jungen Alternative Mecklenburg-Vorpommern (November 2021 bis November 2022), Mitarbeiter der AfD-Fraktion Mecklenburg-Vorpommern (2017 bis 2021)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
