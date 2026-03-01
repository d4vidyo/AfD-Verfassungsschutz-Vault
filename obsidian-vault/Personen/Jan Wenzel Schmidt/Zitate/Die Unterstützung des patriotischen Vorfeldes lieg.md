---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2023-01-12
topic: Sonstiges
page_bfv: 781
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 12.1.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Die Unterstützung des patriotischen Vorfeldes liegt uns sehr am Herzen. Für eine patriotische Wende braucht es auch die wichtige Arbeit außerparlamentarischer Akteure. Deshalb haben Kay Gottschalk und ich dem patriotischen Hausprojekt Castell Aurora 1.500 Euro gespendet. Besucht doch mal die Seite unserer Freunde aus Österreich.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 781

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