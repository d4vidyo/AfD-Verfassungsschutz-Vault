---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-09-08
topic: Sonstiges
page_bfv: 758
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 8.9.2023 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Ich bin ja auch noch hier heute, um Ihnen zunächst beiden [Anm.: Ellen Kositza und Götz Kubitschek] zu danken. [...] Sie haben immer gestanden, sie hatten die richtigen Hinweise, sie haben die richtigen Ratschläge gegeben. Ich wäre nicht Spitzenkandidat ohne Ihrer beider Hilfe. Insofern vielen Dank dafür.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 758

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