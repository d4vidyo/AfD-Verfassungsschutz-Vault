---
type: zitat
speaker: "[[Norbert Kleinwächter]]"
date: 2023-10-11
topic: Menschenwürde
page_bfv: 529
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Norbert Kleinwächter]] vom 11.10.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>#Hamas ist eine Terrororganisation. Als du in die #AfD eingetreten bist, war diese noch gegen islamistischen Terror. Den unterbindet und vernichtet man. Das Existenzrecht und die Sicherheit #lsraels sind unverhandelbar. Auch deshalb sind wir Teil des #Westens.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 529. Antwort auf einen Post vom 11.10.2023

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