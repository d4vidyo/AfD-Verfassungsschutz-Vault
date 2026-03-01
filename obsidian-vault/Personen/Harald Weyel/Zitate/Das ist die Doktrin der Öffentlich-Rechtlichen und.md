---
type: zitat
speaker: "[[Harald Weyel]]"
date: 2024-09-09
topic: Demokratieprinzip
page_bfv: 558
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Harald Weyel]] vom 9.9.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Das ist die Doktrin der Öffentlich-Rechtlichen und auch der Privaten, die ja über Gelder von Staatsaufträgen, Werbeeinnahmen abhängig sind. Die freien Medien sind das Scharnier in die Öffentlichkeit und umgekehrt sollten die freien Medien das Scharnier sein in unser Parteileben. Das heißt, ich kann mich gut damit anfreunden, mit dem Gedanken, dass unsere Interviews, unsere Originaltöne, unsere Reportagen über unsere Partei und unsere Sachpolitik eher von den freien Medien dargestellt wird, als von der Qualitäts... sogenannten Qualitätspresse, die uns eigentlich nur in die Pfanne haut.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 558

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