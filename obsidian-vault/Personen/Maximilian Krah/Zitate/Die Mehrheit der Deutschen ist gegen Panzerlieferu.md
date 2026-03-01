---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-01-08
topic: Demokratieprinzip
page_bfv: 549
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 8.1.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die Mehrheit der Deutschen ist gegen Panzerlieferungen an die #Ukraine. Die Regierung liefert dennoch. Weil sie nicht dem Volk verpflichtet ist, sondern ausländischen Mächten. Wir müssen über Souveränität sprechen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 549

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