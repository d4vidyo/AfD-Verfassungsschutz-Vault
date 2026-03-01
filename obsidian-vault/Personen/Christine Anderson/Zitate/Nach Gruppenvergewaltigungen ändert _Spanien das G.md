---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2022-05-27
topic: Menschenwürde
page_bfv: 342
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 27.5.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Nach Gruppenvergewaltigungen ändert #Spanien das Gesetz: Sexuelle Handlungen brauchen künftig die ausdrückliche Zustimmung aller Beteiligten. ,Nur Ja heißt Ja‘ - das hält #Migranten wie in #Deutschland sicher nicht auf!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 342

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