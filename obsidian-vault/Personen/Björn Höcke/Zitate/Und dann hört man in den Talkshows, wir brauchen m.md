---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-08-31
topic: Menschenwürde
page_bfv: 288
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 31.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und dann hört man in den Talkshows, wir brauchen mehr Polizisten, wir brauchen ein Messerverbot. Nein, liebe Freunde, das Messer ist nicht das Problem, der Messermann ist das Problem. Stell mir mal vor, ja, meine Kinder, meine Buben, die sind mit Schnitzmessern in den Wald gegangen, um sich Pfeil und Bogen zu schnitzen. Jeder Pfadfinder hat ein Messer an der Seite und trägt es mit Stolz. Wir Deutschen haben kein Problem, mit dem Messer sorgsam umzugehen. Das Problem ist, dass die Kartellparteien Millionen haben einwandern lassen, die aus archaischen Kontexten kommen, wo das Recht des Stärkeren gilt, wo das Faustrecht und das Messerrecht gilt. Und das war vorherzusehen. Das Desaster war ein Desaster mit Ansage. Das war verantwortungslose Politik in Reinform. Nochmal, nicht das Messer ist das Problem, der Messermann. Und der muss in Größenordnung dieses Land verlassen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 288

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