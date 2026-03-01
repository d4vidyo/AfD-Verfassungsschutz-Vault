---
type: zitat
speaker: "[[Reimond Hoffmann]]"
date: 2022-08-02
topic: Menschenwürde
page_bfv: 396
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Reimond Hoffmann]] vom 2.8.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wir haben Platz' schreien sie. 'Wohnraum ist zu teuer' schreien sie auch. Wir haben die Lösung: Abschieben schafft Wohnraum!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 396

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