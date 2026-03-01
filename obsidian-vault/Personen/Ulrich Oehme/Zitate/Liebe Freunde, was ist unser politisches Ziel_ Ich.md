---
type: zitat
speaker: "[[Ulrich Oehme]]"
date: 2023-08-04
topic: Menschenwürde
page_bfv: 425
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Ulrich Oehme]] vom 4.8.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Liebe Freunde, was ist unser politisches Ziel? Ich will, dass die europäischen Völker ohne Angst leben können. Das bedeutet Grenzen zu, Remigration! Jetzt!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 425. Bewerbungsrede auf der Europawahlversammlung der AfD

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