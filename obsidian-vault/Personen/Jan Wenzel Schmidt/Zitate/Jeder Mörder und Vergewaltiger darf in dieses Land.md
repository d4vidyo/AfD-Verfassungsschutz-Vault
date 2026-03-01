---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2024-01-28
topic: Sonstiges
page_bfv: 784
source: 'Instagram'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 28.1.2024 veröffentlicht auf: 'Instagram'
> [!quote] Aussage
>Jeder Mörder und Vergewaltiger darf in dieses Land einreisen, bekommt zum Teil dutzende Identitäten und Bürgergeld! Solidarität mit Martin Sellner!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 784

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