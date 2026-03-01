---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2021-05-03
topic: Demokratieprinzip
page_bfv: 626
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom 3.5.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Staatsstreich! Das Bundesverfassungsgericht hat sich zum willigen Erfüllungsgehilfen einer zukünftigen Öko-Diktatur degradiert! Damit ist nach den Medien (genannt 4. Gewalt), der Exekutive und der Legislative auch die Judikative (zumindest das oberste Gericht) offensichtlich größtenteils in der Hand derer, die Deutschland zu einem totalitären, antifreiheitlichen Staat umbauen wollen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 626

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

---
## Meine Auswertung:

**Meine Bewertung:** `INPUT[inlineSelect(option(Unbewertet), option(Legitim), option(Fragwürdig), option(Nicht legitim), defaultValue(Unbewertet)):status]`

_Mein Kommentar:_ 


---
# Nächste Aussage:
```dataview
TABLE speaker AS "Person", date AS "Datum", topic AS "Thema", choice(speaker.is_still_member, "Ja", "Nein") AS "Noch Mitglied?"
FROM "Personen"
WHERE type = "zitat" and status = "Unbewertet" AND file.name != this.file.name
SORT speaker.is_still_member DESC, speaker.relevance ASC, speaker ASC, date ASC
LIMIT 10
```