---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2025-01-24
topic: Demokratieprinzip
page_bfv: 969
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 24.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wer erinnert sich noch an ein Deutschland, in dem Recht und Ordnung herrschte? Ohne Hunderttausende illegale Migranten? Ohne tägliche Messerangriffe und Gruppenvergewaltigungen? Wahrscheinlich ist dieser Mangel an Vorstellungskraft ein Ergebnis der Manipulation des herrschenden Politmedienkartells, das Angst um seine Macht hat?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 969

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