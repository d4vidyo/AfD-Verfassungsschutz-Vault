---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2022-12-11
topic: Menschenwürde
page_bfv: 212
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 11.12.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Die Masse der Deutschen wird diese fatalen Zustände der Ersetzungsmigration und der Kultur- und Staatszersetzung durch die illegale Migration der Dritten Welt mitten in der eigenen Heimat nicht mehr hinnehmen! [...] Der selbst verursachte Fachkräftemangel in Deutschland wird durch die illegale Massenmigration nicht behoben. [...] Wenn die Deutschen diese Erkenntnis nicht haben werden und demnächst nicht millionenfach umdenken, dann war es das mit Deutschland! Dann haben wir die Fremdherrschaft in den Städten und können uns assimilieren als Einheimische.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 212

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