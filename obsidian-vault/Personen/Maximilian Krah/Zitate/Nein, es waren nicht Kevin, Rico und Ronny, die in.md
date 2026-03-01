---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-01-04
topic: Menschenwürde
page_bfv: 276
source: 'Deutschland-Kurier'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 4.1.2023 veröffentlicht auf: 'Deutschland-Kurier'
> [!quote] Aussage
>Nein, es waren nicht Kevin, Rico und Ronny, die in der Silvesternacht in Düsseldorf, Köln, Berlin und anderswo Polizisten mit Feuerwerkskörpern beschossen und die Innenstädte deutscher Städte in bürgerkriegsähnliche Zustände getaucht haben. Es waren Ali Baba und die vierzig Räuber. Was wir hier erleben, ist nicht schlechter Umgang mit Feuerwerkskörpern. Es sind die Folgen von Einwanderung. Seit 2015 wissen wir, was auf uns zukommt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 276

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