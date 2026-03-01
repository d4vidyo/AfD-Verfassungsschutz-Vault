---
type: zitat
speaker: "[[Martin Sichert]]"
date: 2022-10-22
topic: Demokratieprinzip
page_bfv: 648
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Martin Sichert]] vom 22.10.2022 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Das ist eigentlich [...] es ist eine extremistische Politik, die die Regierung betreibt. Die würde in nahezu jedem Land der Welt als extremistisch betrachtet werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 648

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