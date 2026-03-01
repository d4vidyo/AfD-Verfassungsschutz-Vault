---
type: zitat
speaker: "[[Christina Baum]]"
date: 2024-02-08
topic: Sonstiges
page_bfv: 837
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 8.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Kein Verfassungsschutzgutachten und auch nicht dieser aktuelle Gerichtsbeschluss sollten uns davon abhalten, an der Seite unserer Jungen Alternative für Deutschland zu stehen. \<Bild Ich stehe zu unserer Jugend! Sie sind die Zukunft der AfD und die Zukunft für Deutschland!\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 837

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