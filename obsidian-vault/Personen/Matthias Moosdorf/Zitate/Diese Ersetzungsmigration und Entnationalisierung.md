---
type: zitat
speaker: "[[Matthias Moosdorf]]"
date: 2024-02-07
topic: Menschenwürde
page_bfv: 211
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Moosdorf]] vom 7.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Diese Ersetzungsmigration und Entnationalisierung untergraben aber die Grundlagen unserer auf solidarischen Zusammenhalt beruhenden Demokratie und unserer Sozialsysteme.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 211

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