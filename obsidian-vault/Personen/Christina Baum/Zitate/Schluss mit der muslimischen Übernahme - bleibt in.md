---
type: zitat
speaker: "[[Christina Baum]]"
date: 2024-07-10
topic: Menschenwürde
page_bfv: 464
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 10.7.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Schluss mit der muslimischen Übernahme - bleibt in Euren Heimatländern! [...] Ich kann gut verstehen, warum die Regierung nicht preisgeben will, wieviele Muslime mittlerweile in Deutschland leben. [...] Bei dieser rasanten Entwicklung wird es nicht mehr lange dauern und wir Deutschen werden zur Minderheit in der eigenen Heimat.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 464

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