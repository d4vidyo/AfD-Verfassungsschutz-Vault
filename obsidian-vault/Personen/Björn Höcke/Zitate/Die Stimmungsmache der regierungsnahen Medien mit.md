---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2021-12-21
topic: Demokratieprinzip
page_bfv: 611
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 21.12.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Stimmungsmache der regierungsnahen Medien mit ihren immer neuen Corona-Bedrohungsszenarien kann keinen aufgeklärten Demokraten in seinem Urteil mehr täuschen: Deutschland ist kein Rechtsstaat mehr!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 611

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