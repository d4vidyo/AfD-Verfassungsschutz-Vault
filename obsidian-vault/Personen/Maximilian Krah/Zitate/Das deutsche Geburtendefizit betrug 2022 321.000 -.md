---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-05-03
topic: Menschenwürde
page_bfv: 210
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 3.5.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Das deutsche Geburtendefizit betrug 2022 321.000 - also mehr Tote als Neugeborene. Gleichzeitig sind knapp 1,5 Millionen Menschen mehr ein- als ausgewandert. Das ist Ersetzungsmigration.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 210

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