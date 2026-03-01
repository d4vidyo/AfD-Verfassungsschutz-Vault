---
type: zitat
speaker: "[[Anna Leisten]]"
date: 2024-12-03
topic: Sonstiges
page_bfv: 863
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Anna Leisten]] vom 3.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Eine Auflösung unserer Organisation ist zum jetzigen Zeitpunkt völlig falsch, und wir haben viele andere wichtige Aufgaben zu meistern. Wir stecken aktuell in den Vorbereitungen unserer Jugendkampagne zur Bundestagswahl 2025 – wir freuen uns auf einen guten Wahlkampf mit allen Landesverbänden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 863

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