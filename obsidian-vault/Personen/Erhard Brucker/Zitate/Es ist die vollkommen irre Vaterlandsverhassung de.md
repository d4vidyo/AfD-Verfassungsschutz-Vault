---
type: zitat
speaker: "[[Erhard Brucker]]"
date: 2022-07-30
topic: Menschenwürde
page_bfv: 135
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Erhard Brucker]] vom 30.7.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Es ist die vollkommen irre Vaterlandsverhassung der – egal ob rot/rot ; rot, grün angestrichen Sozialisten, die sich den Untergang der autochthonen Bevölkerung regelrecht herbeisehnt. [...] Was die aber nicht verstanden haben ist: die Flutung Europas mit Musels wird letztlich dazu führen, dass sie die ersten Opfer sein werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 135

**Verfassungsschutz Kategorisierung:** Verstoß gegen die Menschenwürde.

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