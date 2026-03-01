---
type: zitat
speaker: "[[Rainer Rothfuß]]"
date: 2025-01-11
topic: Demokratieprinzip
page_bfv: 950
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Rainer Rothfuß]] vom 11.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir wollen nicht mehr der Vasall und die Melkkuh Brüssels sein und auch nicht mehr Washingtons, sondern wir wollen einfach unseren eigenen Standpunkt entwickeln. Wir wollen den eigenen Interessen dienen. Wir wollen gute konstruktive Beziehungen haben nach Westen wie nach Osten, und das taugt eben denen in Brüssel nicht, die meinen, die Richtung vorgeben zu können.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 950

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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