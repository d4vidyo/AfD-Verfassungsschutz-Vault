---
type: zitat
speaker: "[[Gereon Bollmann]]"
date: 2023-01-26
topic: Menschenwürde
page_bfv: 298
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gereon Bollmann]] vom 26.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Palästinensischer Messerstecher läuft Amok: Importierte Messergewalt wird totgeschwiegen! Eine Bluttat erschüttert Schleswig-Holstein. Tatort Regionalexpress: Zwei Tote, sieben Verletzte. Das ist die verheerende Bilanz der Bluttat im Regionalexpress RE 70 auf der Strecke Kiel-Hamburg.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 298

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