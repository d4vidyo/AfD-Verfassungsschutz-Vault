---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-02-07
topic: Sonstiges
page_bfv: 834
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 7.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Deswegen bin ich stolz auf unsere Jugend, die den freiheitlich-demokratischen Geist und das rechtsstaatliche Denken der alten Bundesrepublik nicht mehr aus eigenem Erleben kennt und trotzdem mutig für diese Werte eintritt. In einer Zeit des politischen Umbruchs, die Gefahr läuft, in einen neuen Obrigkeitsstaat einzumünden, ist es besonders wichtig, daß alle Freiheitsfreunde zusammenhalten. Wir Älteren, die noch den direkten Vergleich haben, müssen uns vor unsere Parteijugend stellen. Gemeinsam treten wir für eine freiheitliche Demokratie ein. Wir stellen uns gegen einen Extremismus von Oben, gegen den Regierungsextremismus, der von keinem Verfassungsschutz bekämpft, sondern viel mehr exekutiert wird.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 834

**Verfassungsschutz Kategorisierung:** Sonstiges.

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