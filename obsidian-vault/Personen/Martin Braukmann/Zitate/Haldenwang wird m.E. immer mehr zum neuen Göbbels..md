---
type: zitat
speaker: "[[Martin Braukmann]]"
date: 2023-04-26
topic: Demokratieprinzip
page_bfv: 583
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Braukmann]] vom 26.4.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Haldenwang wird m.E. immer mehr zum neuen Göbbels. Seine Interpretation des Grundgesetzes wird zum Maßstab erhoben. Alles andere ist rechtsextrem. Widerlich und demokratiefeindlich.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 583

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