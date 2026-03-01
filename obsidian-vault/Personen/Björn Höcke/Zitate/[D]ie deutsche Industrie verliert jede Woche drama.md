---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-10-03
topic: Demokratieprinzip
page_bfv: 546
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 3.10.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>[D]ie deutsche Industrie verliert jede Woche dramatisch an Konkurrenzfähigkeit, hunderte energieintensive Unternehmen haben bereits ihre Produktion eingestellt, immer mehr kehren Deutschland den Rücken [...]. Es ist bitter, aber es ist so: Die US-amerikanische Regierung befiehlt der deutschen Regierung den wirtschaftlichen Selbstmord und Scholz & Co. führen ihn aus!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 546

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