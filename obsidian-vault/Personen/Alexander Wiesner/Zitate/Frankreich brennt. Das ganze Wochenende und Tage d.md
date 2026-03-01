---
type: zitat
speaker: "[[Alexander Wiesner]]"
date: 2023-07-05
topic: Menschenwürde
page_bfv: 448
source: 'X (ehemals Twitter)/Instagram'
status: Unbewertet
---

# Zitat: [[Alexander Wiesner]] vom 5.7.2023 veröffentlicht auf: 'X (ehemals Twitter)/Instagram'
> [!quote] Aussage
>Frankreich brennt. Das ganze Wochenende und Tage darauf gab es schwerste Ausschreitungen von muslimisch-stämmigen Bevölkerungsgruppen, welche das Land in bürgerkriegsähnliche Zustände gestürzt haben. Für uns muss das ein Weckruf sein. Diese Menschen, diese Kulturkreise sind mit einer westlichen Demokratie nicht vereinbar und in unsere Gesellschaft auch nach Jahrzehnten nicht integrierbar. Deswegen Remigration jetzt!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 448

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