---
type: zitat
speaker: "[[Stephan Protschka]]"
date: 2021-12-01
topic: Rechtsstaatsprinzip
page_bfv: 665
source: 'None'
status: Unbewertet
---

# Zitat: [[Stephan Protschka]] vom 1.12.2021 veröffentlicht auf: 'None'
> [!quote] Aussage
>Wenn sich Leute da intern was an den Kopf schmeißen, gehört das doch auch zur freiheitlich demokratischen Grundordnung dazu, dass man verschiedener Meinung ist.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 665

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Rechtsstaatsprinzip.

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