---
type: zitat
speaker: "[[Uwe Schulz]]"
date: Nicht Verfügbar
topic: Menschenwürde
page_bfv: 265
source: 'Flyer'
status: Unbewertet
---

# Zitat: [[Uwe Schulz]] vom None veröffentlicht auf: 'Flyer'
> [!quote] Aussage
>In den Jahren der politisch gewollten steigenden Zuwanderung aus kulturfremden Ländern nach Mitteleuropa steigen die Kriminalitätsraten in erschreckender Weise. Messermorde, Gruppenvergewaltigungen, Rohheitsdelikte sind ungebremst auf dem Vormarsch.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 265

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