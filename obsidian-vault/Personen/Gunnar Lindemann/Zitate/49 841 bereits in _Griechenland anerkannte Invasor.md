---
type: zitat
speaker: "[[Gunnar Lindemann]]"
date: 2022-08-01
topic: Menschenwürde
page_bfv: 370
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Gunnar Lindemann]] vom 1.8.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>49 841 bereits in #Griechenland anerkannte Invasoren haben It. dt. Innenministerium in #Deutschland erneut Asyl beantragt. Und sie dürfen hier bleiben,weil es in Griechenland, wo Deutsche Urlaub machen, so schlimm ist. Es gibt halt mehr Geld in Germoney.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 370

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