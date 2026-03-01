---
type: zitat
speaker: "[[Uwe Detert]]"
date: 2023-11-01
topic: Demokratieprinzip
page_bfv: 542
source: 'Welt am Sonntag'
status: Unbewertet
---

# Zitat: [[Uwe Detert]] vom November 2023 veröffentlicht auf: 'Welt am Sonntag'
> [!quote] Aussage
>Das Deutsche Reich ist da - Es ist nie untergegangen - Es war in kein Kriegsgeschehen verwickelt - Es gehört uns.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: November 2023

**SPIEGEL-Notiz:** Gutachten Seite: 542

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