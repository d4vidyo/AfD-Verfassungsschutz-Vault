---
type: zitat
speaker: "[[Daniel Haseloff]]"
date: 2022-11-30
topic: Menschenwürde
page_bfv: 199
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Daniel Haseloff]] vom 30.11.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Sozial-Tourismus: Die Deutschen werden systematisch ausgetauscht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 199

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