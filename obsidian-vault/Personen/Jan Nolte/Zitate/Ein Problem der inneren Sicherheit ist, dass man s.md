---
type: zitat
speaker: "[[Jan Nolte]]"
date: 2024-10-14
topic: Menschenwürde
page_bfv: 260
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Jan Nolte]] vom 14.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ein Problem der inneren Sicherheit ist, dass man sich aus Gründen der Political Correctness weitgehend weigert, anzuerkennen, dass wir seit Jahren massive Migration von Menschen haben, die tendenziell viel Gewaltaffiner sind, als der autochthone Deutsche. Man versucht Menschen, die ein ganz anderes Verhältnis zu Gewalt und 'Ehre' haben, in der Familie viel öfter mit Gewalt konfrontiert sind und die oft in einem völlig anderen sozialen Gefüge leben, als der autochthone Deutsche, mit Präventions- und Repressionsinstrumenten zu begegnen, die für eine andere Gesellschaft konzipiert sind. Vorstrafen und Gefängnisaufenthalte, werden in bestimmten Parallelgesellschaften als Zeichen der Stärke gesehen. Und wer ohnehin keine normale Karriere im Arbeitsmarkt plant, den stört auch der 'Knick' in der Vita nicht. Gilt so natürlich nicht für jeden, ist aber grundsätzlich ein gut beobachtbares Problem.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 260

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