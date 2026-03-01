---
type: zitat
speaker: "[[Georg Hock]]"
date: 2021-06-01
topic: Rechtsstaatsprinzip
page_bfv: 665
source: 'None'
status: Unbewertet
---

# Zitat: [[Georg Hock]] vom Juni 2021 veröffentlicht auf: 'None'
> [!quote] Aussage
>Bekämpft bitte (oder auch gefälligst) mit dem vielen Geld, das ihr vier lange Jahre egal in welcher Partei bekommt, das Deutschland meuchelnde System. Das erwarten unsere Wähler. Der Widerstand der Straße würde es Euch danken.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: Juni 2021

**SPIEGEL-Notiz:** Gutachten Seite: 665

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