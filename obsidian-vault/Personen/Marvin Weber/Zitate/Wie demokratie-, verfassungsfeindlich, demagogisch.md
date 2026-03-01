---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2024-02-06
topic: Demokratieprinzip
page_bfv: 618
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 6.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wie demokratie-, verfassungsfeindlich, demagogisch, korrupt, korrumpiert, psychopathisch, totalitär und faschistoid die Regierungskaste in Deutschland ist, konnte jeder Bürger beim Impfzwang-Verbrechen während der der Willkürherrschaft der Altparteien in der Coronazeit sehen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 618

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