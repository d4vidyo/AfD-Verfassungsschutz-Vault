---
type: zitat
speaker: "[[Sebastian Wippel]]"
date: 2022-12-06
topic: Menschenwürde
page_bfv: 353
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Sebastian Wippel]] vom 6.12.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Eritreer sticht zwei Mädchen in Illerkirchberg nieder, eines verstirbt- Die nächsten Opfer von Massenmigration und Asylindustrie! [...] Das ist das beste Deutschland aller Zeiten, von welchem politisch und medial immer wieder geschwärmt wird. Das ist die bunte Multikultopie, die wir uns alle gefälligst für die Zukunft zu wünschen haben. Und vor allem: Das ist der nächste ,Einzelfall‘, der auf das Konto derjenigen geht, die seit dem Jahre 2015 die ungehemmte Massenmigration in unser Land vorantreiben und gutheißen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 353

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