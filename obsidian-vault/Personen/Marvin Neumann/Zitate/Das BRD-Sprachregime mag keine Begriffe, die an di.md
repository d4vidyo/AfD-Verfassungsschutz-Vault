---
type: zitat
speaker: "[[Marvin Neumann]]"
date: 2025-01-13
topic: Demokratieprinzip
page_bfv: 966
source: 'X (ehemals Twitter), Repost'
status: Unbewertet
---

# Zitat: [[Marvin Neumann]] vom 13.1.2025 veröffentlicht auf: 'X (ehemals Twitter), Repost'
> [!quote] Aussage
>Das BRD-Sprachregime mag keine Begriffe, die an die Existenz von Abstammungsdeutschen erinnern. Nicht sonderlich überraschend, aber wieder symptomatisch für einen ethnozidal-antideutsch ausgearteten Verfassungspluralismus.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 966

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