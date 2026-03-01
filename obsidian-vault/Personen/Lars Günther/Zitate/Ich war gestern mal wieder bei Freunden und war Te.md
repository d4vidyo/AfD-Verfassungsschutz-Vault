---
type: zitat
speaker: "[[Lars Günther]]"
date: 2022-07-20
topic: Sonstiges
page_bfv: 729
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Lars Günther]] vom 20.7.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ich war gestern mal wieder bei Freunden und war Teil der täglichen Nachrichtensendungen: COMPACT - Der Tag.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 729

**Verfassungsschutz Kategorisierung:** Sonstiges.

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