---
type: person
name: Marc Jongen
gender: male
state: Baden-Württemberg
is_still_member: true
id: 078
relevance: 3
---

# Zur Person Marc Jongen
> [!info] 
>Europaabgeordneter (seit Juli 2024), Bundestagsabgeordneter für Baden-Württemberg (September 2017 bis Juli 2024), Bundesvorstandsmitglied (Juni 2022), Vorsitzender im Landesverband Baden-Württemberg (März 2017 bis Februar 2019), Landesvorstandsmitglied Baden-Württemberg (2013 bis Februar 2024), Kuratoriumsmitglied der parteinahen Desiderius-Erasmus-Stiftung (seit Juli 2018)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
