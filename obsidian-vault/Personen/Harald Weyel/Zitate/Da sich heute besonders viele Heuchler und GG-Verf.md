---
type: zitat
speaker: "[[Harald Weyel]]"
date: 2024-05-23
topic: Demokratieprinzip
page_bfv: 579
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Harald Weyel]] vom 23.5.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Da sich heute besonders viele Heuchler und GG-Verfassungsrealitäten-Brecher des Themas medial bemächtigen, mal bitte zurück auf Anfang: 'Der Staat ist um des Menschen willen da, nicht der Mensch um des Staates willen.' Artikel 1 des Entwurfs, den... #GG [...] 75 Jahre Grundgesetz | Deutschlands faktisches Ein-Parteien-Regime inszeniert Jubelfeiern während die - prominenten Dissidenten im Gefängnis - oder im Ausland sitzen - die einzige Opposition verboten werden soll - und Regierungskritik 'unterhalb der Strafbarkeit' vom Geheimdienst verfolgt wird.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 579

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