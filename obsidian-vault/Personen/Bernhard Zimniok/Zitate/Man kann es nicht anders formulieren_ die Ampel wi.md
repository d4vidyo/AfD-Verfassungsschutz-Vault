---
type: zitat
speaker: "[[Bernhard Zimniok]]"
date: 2024-04-04
topic: Menschenwürde
page_bfv: 194
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Bernhard Zimniok]] vom 4.4.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Man kann es nicht anders formulieren: die Ampel wirbt aktiv für den Bevölkerungsaustausch!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 194

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