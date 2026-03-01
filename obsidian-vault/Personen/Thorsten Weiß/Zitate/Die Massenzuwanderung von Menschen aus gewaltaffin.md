---
type: zitat
speaker: "[[Thorsten Weiß]]"
date: 2025-01-23
topic: Menschenwürde
page_bfv: 924
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Thorsten Weiß]] vom 23.1.2025 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Die Massenzuwanderung von Menschen aus gewaltaffinen mittelalterlichen Kulturen ist tödlich. Trotzdem wird diese Entwicklung gefördert und Abschiebungen planmäßig verhindert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 924

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