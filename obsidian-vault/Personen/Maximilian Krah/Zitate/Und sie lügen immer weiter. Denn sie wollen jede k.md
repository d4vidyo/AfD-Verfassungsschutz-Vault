---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2022-05-21
topic: Menschenwürde
page_bfv: 168
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 21.5.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Und sie lügen immer weiter. Denn sie wollen jede kulturelle Identität zerstören. #Einwanderung

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 168

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