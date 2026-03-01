---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-09-28
topic: Demokratieprinzip
page_bfv: 568
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 28.9.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ihr habt die 'anständigen Leute' von #CDU und #BSW gezwungen, die Masken fallen zu lassen. Sie delegitimieren sich und damit geht die Herrschaft der Kartellparteien zuende.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 568

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