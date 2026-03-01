---
type: zitat
speaker: "[[Matthias Moosdorf]]"
date: 2022-05-25
topic: Menschenwürde
page_bfv: 495
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Moosdorf]] vom 25.5.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Sollte sich der HERR nicht seiner erbarmen? Auch wenn es sich um einen der größten Verbrecher und den Verursacher von soviel Leid, Idiotie und Unkultur handelt? ICH glaube nämlich, MIT Soros droht das Ende Europas.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 495

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