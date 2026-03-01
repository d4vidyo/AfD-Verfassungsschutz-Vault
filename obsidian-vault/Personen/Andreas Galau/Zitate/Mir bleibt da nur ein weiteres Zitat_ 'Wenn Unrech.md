---
type: zitat
speaker: "[[Andreas Galau]]"
date: 2021-11-30
topic: Rechtsstaatsprinzip
page_bfv: 662
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Andreas Galau]] vom 30.11.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Mir bleibt da nur ein weiteres Zitat: 'Wenn Unrecht zu Recht wird, wird #Widerstand zu Pflicht und Gehorsam ist Verbrechen!'

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 662

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