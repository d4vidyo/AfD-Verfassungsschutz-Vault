---
type: zitat
speaker: "[[Miguel Klauß]]"
date: 2024-01-10
topic: Menschenwürde
page_bfv: 419
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Miguel Klauß]] vom 10.1.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Wieso Geheimplan gegen Deutschland? Es ist ein Plan für Deutschland. Mio fach Abschiebungen von illegalen Migranten ist richtig und wichtig. Wir haben auch passend dazu den legendären @Abschiebekalender. Nur noch #AfD

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 419

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