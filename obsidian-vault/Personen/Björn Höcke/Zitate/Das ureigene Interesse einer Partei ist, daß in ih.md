---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2023-12-21
topic: Sonstiges
page_bfv: 765
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 21.12.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Das ureigene Interesse einer Partei ist, daß in ihrem Vorfeld keine unberechenbaren extremistischen Bewegungen oder radikale Konkurrenzparteien entstehen. [...] Distanzierung, Abgrenzung und Ignoranz bewirken das Gegenteil und schaden somit auch dem Eigeninteresse der Partei.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 765. Höcke zitiert aus einem Buch von Martin Sellner.

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