---
type: person
name: Martin Sichert
gender: male
state: Bayern
is_still_member: true
id: 112
relevance: 4
---

# Zur Person Martin Sichert
> [!info] 
>Bundestagsabgeordneter für Niedersachsen (seit Februar 2025), Bundestagsabgeordneter für Bayern (September 2017 bis Februar 2025), Vorsitzender im Landesverband Bayern (November 2017 bis 2019), stv. Vorsitzender im Landesverband Bayern (2013 bis 2014), Mitglied des Bundeskonvents (ab 2015)
>
>**_Ist die Person noch Mitglied:_ Ja**

---
## Alle Zitate zur Auswertung
```dataview
TABLE date AS "Datum", topic AS "Thema", choice(status = "Legitim", "<span style='color: lightgreen; font-weight:bold;'>Legitim</span>", choice(status = "Fragwürdig", "<span style='color: #f9e2af; font-weight:bold;'>Fragwürdig</span>", choice(status = "Nicht legitim", "<span style='color: tomato; font-weight:bold;'>Nicht Legitim</span>", "<span style='color: gray;'>Unbewertet</span>") ) ) AS "Bewertung"
WHERE speaker = this.file.link AND type = "zitat"
SORT choice(status = "Unbewertet", 1, choice(status = "Legitim", 2, choice(status = "Fragwürdig", 3, choice(status = "Nicht legitim", 4, 5)))) ASC, date ASC
```
