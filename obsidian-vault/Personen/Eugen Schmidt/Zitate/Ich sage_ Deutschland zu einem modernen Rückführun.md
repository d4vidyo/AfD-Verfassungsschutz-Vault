---
type: zitat
speaker: "[[Eugen Schmidt]]"
date: 2022-06-01
topic: Menschenwürde
page_bfv: 401
source: 'Instagram'
status: Unbewertet
---

# Zitat: [[Eugen Schmidt]] vom Juni 2022 veröffentlicht auf: 'Instagram'
> [!quote] Aussage
>Ich sage: Deutschland zu einem modernen Rückführungsland machen!

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: Juni 2022

**SPIEGEL-Notiz:** Gutachten Seite: 401. abweichendes Datum in der Fußnote: 10.7.2022

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