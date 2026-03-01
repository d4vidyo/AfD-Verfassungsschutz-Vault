---
type: person
name: Birgit Bessin
gender: female
state: Brandenburg
is_still_member: true
id: 083
relevance: 4
---

# Zur Person Birgit Bessin
> [!info] 
>Bundestagsabgeordnete für Brandenburg (seit Februar 2025), Landtagsabgeordnete in Brandenburg (Oktober 2014 bis März 2025), stv. Vorsitzende der AfD-Fraktion im Landtag Brandenburg (Oktober 2017 bis Frühjahr 2022), parlamentarische Geschäftsführerin der AfD-Fraktion im Landtag Brandenburg (Oktober 2014 bis Dezember 2017), Vorsitzende im Landesverband Brandenburg (April 2022 bis April 2024), stv. Vorsitzende im Landesverband Brandenburg (Juli 2016 bis April 2022), Landesvorstandsmitglied Brandenburg (Herbst 2013 bis Frühjahr 2015)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
