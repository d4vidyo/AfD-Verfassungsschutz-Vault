---
type: zitat
speaker: "[[Alexander Sell]]"
date: 2023-07-30
topic: Menschenwürde
page_bfv: 448
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Alexander Sell]] vom 30.7.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Ich habe deshalb noch an einer Mittelschule in den Pariser Außenbezirken Deutsch unterrichtet, also im Banlieue, schon damals ein Kriegsgebiet. Die Mutter eines Schülers, eine Deutsche, erzählte mir bei einer Gelegenheit, dass in dem Hochhaus, in dem sie leben, jedes Jahr zum islamischen Opferfest dickes Blut aus den Abflüssen quellt. Warum? Weil die muslimischen Nachbarn in den oberen Stockwerken Schafe und Ziegen in den Badewannen schächten. [...]. Die Leidtragenden der Masseneinwanderung nach Europa sind die Menschen, die mit diesen Barbaren Tür an Tür leben müssen. Also diejenigen, die nicht einfach wegziehen können oder wollen. Das sind die Menschen, die uns wählen. Das sind die Menschen, deren Interessen wir vertreten, und zwar ausschließlich wir.

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