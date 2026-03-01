---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2023-05-21
topic: Menschenwürde
page_bfv: 506
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 21.5.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Das war der große Gegensatz zu heutigen überstaatlichen Konstrukten wie der Europäischen Union mit ihren 'Transformationsprozessen', der das Wesen eines Obrigkeits-Projektes anhaftet, das den Bürgern zwangsverordnet wird.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 506

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