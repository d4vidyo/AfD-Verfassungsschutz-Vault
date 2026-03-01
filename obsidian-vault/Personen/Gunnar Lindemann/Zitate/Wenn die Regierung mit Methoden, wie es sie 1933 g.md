---
type: zitat
speaker: "[[Gunnar Lindemann]]"
date: 2023-10-30
topic: Demokratieprinzip
page_bfv: 583
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Gunnar Lindemann]] vom 30.10.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wenn die Regierung mit Methoden, wie es sie 1933 gab, gegen die demokratisch gewählte Opposition vorgeht, weiß man, wie es um die Demokratie in #Deutschland bestellt ist.

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