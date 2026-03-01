---
type: zitat
speaker: "[[Roger Beckamp]]"
date: 2022-11-29
topic: Sonstiges
page_bfv: 832
source: 'odysee.com'
status: Unbewertet
---

# Zitat: [[Roger Beckamp]] vom 29.11.2022 veröffentlicht auf: 'odysee.com'
> [!quote] Aussage
>Und dabei bin ich sogar ehrlich gesagt ganz guter Dinge. Weil ich sehe es so bei vielen Leuten bei uns in der Fraktion, bei jungen Leuten, also bei Referenten, oder Praktikanten, die nachwachsen. [...] Also vorwiegend sehr gut ausgebildete, studierte, junge Männer, die sehr idealistisch sind, die sehr, auch, belastbar sind, die Dinge aushalten und nicht irgendwie direkt laufen gehen, wenn es mal böse Presse gibt oder so. [...] Insofern bin ich da, auch was ich so bei der JA mitkriege, oder auch im Vorfeld, bin ich da wirklich guter Dinge.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 832. Interview auf Martin Sellners Kanal.

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