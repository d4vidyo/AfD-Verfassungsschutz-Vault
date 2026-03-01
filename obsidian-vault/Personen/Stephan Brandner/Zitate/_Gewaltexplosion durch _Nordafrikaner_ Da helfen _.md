---
type: zitat
speaker: "[[Stephan Brandner]]"
date: 2024-07-26
topic: Menschenwürde
page_bfv: 260
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Stephan Brandner]] vom 26.7.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>#Gewaltexplosion durch #Nordafrikaner? Da helfen #Grenzkontrollen! #deshalbAfD

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 260

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