---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2025-01-15
topic: Demokratieprinzip
page_bfv: 954
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 15.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Nun möchte die CDU gegen 'ungefilterte Meinungen' vorgehen mithilfe des willfährigen Geheimdienstes/Verfassungsschutzes. Die Blockparteien zeigen immer mehr ihr wahres Gesicht. Das ist Zensur der Meinungsfreiheit.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 954

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