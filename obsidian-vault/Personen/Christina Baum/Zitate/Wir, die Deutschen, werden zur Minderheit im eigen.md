---
type: zitat
speaker: "[[Christina Baum]]"
date: 2023-03-20
topic: Menschenwürde
page_bfv: 245
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 20.3.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wir, die Deutschen, werden zur Minderheit im eigenen Land und dies in einer Geschwindigkeit, das einem schwindlig wird. Vom deutschen Schuldkult psychisch/ seelisch geschwächt und jahrzehntelang umerzogen, wird weiter darauf hin gearbeitet, unser Volk, unsere Kultur, unsere Sprache und unsere Traditionen langsam verschwinden zu lassen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 245

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