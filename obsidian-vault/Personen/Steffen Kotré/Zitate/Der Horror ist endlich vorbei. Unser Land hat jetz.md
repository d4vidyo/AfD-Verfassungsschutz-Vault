---
type: zitat
speaker: "[[Steffen Kotré]]"
date: 2024-12-16
topic: Menschenwürde
page_bfv: 890
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Steffen Kotré]] vom 16.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Der Horror ist endlich vorbei. Unser Land hat jetzt die Möglichkeit, sich gegen Gängelung, Überwachung, Enteignung und Ersetzungsmigration zu wehren. Macht alle mit – jetzt kommt es auf jeden Einzelnen an!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 890

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