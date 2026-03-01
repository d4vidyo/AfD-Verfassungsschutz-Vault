---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2025-02-01
topic: Sonstiges
page_bfv: 871
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 1.2.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die @JA_Deutschland wurde heute einstimmig aufgelöst. Gründen wir die Junge Alternative als neue AfD Jugendorganisation entsprechend der neuen Statuten zeitnah neu. Die AfD braucht als Partei der Zukunft eine starke Jugend!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 871

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