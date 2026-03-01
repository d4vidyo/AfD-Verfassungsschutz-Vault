---
type: zitat
speaker: "[[Tomasz Froelich]]"
date: 2022-02-15
topic: Menschenwürde
page_bfv: 180
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Tomasz Froelich]] vom 15.2.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Der 'Große Austausch' ist kein rechtsextremes Narrativ, auch keine Verschwörungstheorie, sondern ein real stattfindender, durch nüchterne demographische Empirie gestützter, politisch offenkundig gewollter Prozess.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 180

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