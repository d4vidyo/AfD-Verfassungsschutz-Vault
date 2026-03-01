---
type: zitat
speaker: "[[Harald Weyel]]"
date: 2023-10-10
topic: Menschenwürde
page_bfv: 412
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Harald Weyel]] vom 10.10.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Syrer, Afghanen, Iraker sind massiv überrepräsentiert bei Messertätern, die durch die Bundespolizei erfasst werden. Hierfür gibt es eine einzige Lösung: die #Remigration.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 412

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