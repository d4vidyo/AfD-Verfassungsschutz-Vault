---
type: zitat
speaker: "[[Jürgen Braun]]"
date: 2024-03-05
topic: Menschenwürde
page_bfv: 469
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Jürgen Braun]] vom 5.3.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Eine Islamisierung findet nicht statt! Alles nur Verschwörungstheorie [Zwinkerndes Emoji]

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 469

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