---
type: zitat
speaker: "[[Hannes Gnauck]]"
date: Nicht Verfügbar
topic: Sonstiges
page_bfv: 742
source: 'None'
status: Unbewertet
---

# Zitat: [[Hannes Gnauck]] vom None veröffentlicht auf: 'None'
> [!quote] Aussage
>Unterstützungswerten Projekten, die sich für den Erhalt der unserer Heimat einsetzen, werde ich immer unter die Arme greifen.

**Parser-Notiz:** Es handelt sich möglicherweise um ein Duplikat von dem Zitat: [[Unterstützungswerten Projekten, die sich für den E]]

**SPIEGEL-Notiz:** Gutachten Seite: 742

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