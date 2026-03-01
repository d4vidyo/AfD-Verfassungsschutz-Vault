---
type: zitat
speaker: "[[Frank Otto Lizureck]]"
date: 2022-03-20
topic: Demokratieprinzip
page_bfv: 616
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Frank Otto Lizureck]] vom 20.3.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Karl Lauterbach ist die Schädigung von Kindern und Jugendlichen egal. Es muss gespritzt werden bis zum spritzen Endsieg.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 616

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