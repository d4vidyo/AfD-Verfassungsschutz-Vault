---
type: zitat
speaker: "[[Volker Richter]]"
date: 2025-02-02
topic: Demokratieprinzip
page_bfv: 956
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Volker Richter]] vom 2.2.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wie Grüne, SPD und Linke eine Massenpsychose auslösen und dabei den inneren Frieden riskieren. Die Skrupellosigkeit mit der manche Menschen miteinander umgehen, zeigte sich in den vergangenen Jahren in vielen totalitären Systemen. Dabei waren die jeweiligen Ideologien moralische Rechtfertigungen für zutiefst unmenschliches Verhalten. Das ist vielen bekannt, was liegt nun also näher, als eigenes skrupelloses Verhalten einer gegnerischen politischen Kraft zu unterstellen und so entsprechend eine Vielzahl an Menschen, die mit Sicherheit das Gute wollen und nichts böses, für sich zu instrumentalisieren? Hiermit halte ich fest: Diese Methodik der totalitären Herrschaft über die eigene Bevölkerung hat Deutschland voll im Griff.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 956

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