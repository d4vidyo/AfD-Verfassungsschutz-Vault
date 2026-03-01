---
type: zitat
speaker: "[[Gunnar Beck]]"
date: 2022-06-07
topic: Menschenwürde
page_bfv: 376
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Gunnar Beck]] vom 7.6.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Köln Hauptbahnhof – Wer hier einfährt, lässt jede Hoffnung zurück. Dann nirgends zeigt sich Deutschlands #Zukunft als Siedlungsgebiet für Menschen aus #Afrika und dem #Orient klarer als hier.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 376

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