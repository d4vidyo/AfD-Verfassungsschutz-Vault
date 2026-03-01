---
type: zitat
speaker: "[[Daniel Roi]]"
date: 2022-06-24
topic: Menschenwürde
page_bfv: 374
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Daniel Roi]] vom 24.6.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Solange wir keine Festung Europa haben und wirklichen Grenzschutz organisieren, solange wird das so weiter gehen. Die linksliberale Presse wird uns aber nun erklären, dass der Russe schuld ist, weil die alle hungern müssen. Gut informierte Bürger wissen, dass dies nur eine weitere Propagandalüge ist. Die Eroberungsorgien jüngst in #ltalien u. a. am Gardasee werden sich ausweiten...

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 374

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