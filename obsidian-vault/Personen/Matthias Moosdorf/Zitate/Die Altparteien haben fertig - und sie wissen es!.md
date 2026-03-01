---
type: zitat
speaker: "[[Matthias Moosdorf]]"
date: 2023-05-30
topic: Demokratieprinzip
page_bfv: 584
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Moosdorf]] vom 30.5.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Altparteien haben fertig - und sie wissen es! Ideologien haben unser Land zweimal in den letzten 100 Jahren an den Rand des Verderbens geführt. Und es waren kluge, gefährliche, anfangs undurchschaubare Verführungen. Verglichen mit den plumpen, dümmlichen Entscheidungen der Ampel nehmen sie sich aus wie nach Verständnis heischend.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 584

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