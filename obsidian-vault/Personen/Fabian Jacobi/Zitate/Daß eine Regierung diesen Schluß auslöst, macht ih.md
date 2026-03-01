---
type: zitat
speaker: "[[Fabian Jacobi]]"
date: 2021-12-22
topic: Rechtsstaatsprinzip
page_bfv: 661
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Fabian Jacobi]] vom 22.12.2021 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Daß eine Regierung diesen Schluß auslöst, macht ihr Handeln zum Fehler; daß sie es vorsätzlich tut, zum Verbrechen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 661

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Rechtsstaatsprinzip.

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