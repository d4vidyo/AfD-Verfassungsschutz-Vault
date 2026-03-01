---
type: zitat
speaker: "[[Thomas Prantl]]"
date: 2021-11-16
topic: Nationalsozialismus
page_bfv: 675
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Thomas Prantl]] vom 16.11.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Nochmal zur Erinnerung!! Der Nürnberger Kodex wurde eingeführt, damit Menschen nie wieder zu medizinischen Behandlungen GEZWUNGEN oder GENÖTIGT werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 675

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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