---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2022-11-29
topic: Sonstiges
page_bfv: 777
source: 'Interview'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 29.11.2022 veröffentlicht auf: 'Interview'
> [!quote] Aussage
>Jetzt, wo du es sagst...schwierig... Nein. Ich habe die Bedenken lange abgelegt, ehrlich gesagt. Ich rede mit jedem, fast jedem und ganz besonders gerne mit Euch heute Abend.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 777

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