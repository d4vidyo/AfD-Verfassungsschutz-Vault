---
type: zitat
speaker: "[[Volker Richter]]"
date: 2025-01-04
topic: Demokratieprinzip
page_bfv: 951
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Volker Richter]] vom 4.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Sie haben Schützenhilfe von der vierten Macht im Staat, welche sich nicht als freie und unabhängige Journalisten begreifen, sondern ihre persönliche politische Meinung in einer Form des Erziehungsjournalismus zu Tage bringen, die jeder Beschreibung spottet.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 951

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