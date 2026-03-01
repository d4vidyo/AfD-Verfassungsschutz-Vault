---
type: zitat
speaker: "[[Damian Lohr]]"
date: 2024-12-17
topic: Sonstiges
page_bfv: 860
source: 'Freilich Magazin'
status: Unbewertet
---

# Zitat: [[Damian Lohr]] vom 17.12.2024 veröffentlicht auf: 'Freilich Magazin'
> [!quote] Aussage
>In jedem Fall würde die neue Struktur für mehr Disziplin sorgen. Dabei geht es gar nicht darum, die Jugendorganisation einzuschränken, aber zumindest entfällt der Blankoscheck für Leute, die sich nicht ihrer Verantwortung für die Partei und Jugendorganisation bewusst sind. Dabei gilt selbstverständlich nicht der VS oder der politische Gegner als Maßstab. Wer groben Unfug produziert, muss diszipliniert werden können.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 860

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