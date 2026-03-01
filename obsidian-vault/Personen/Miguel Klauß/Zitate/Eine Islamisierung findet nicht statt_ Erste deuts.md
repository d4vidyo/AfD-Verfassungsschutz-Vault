---
type: zitat
speaker: "[[Miguel Klauß]]"
date: 2024-03-06
topic: Menschenwürde
page_bfv: 468
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Miguel Klauß]] vom 6.3.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Eine Islamisierung findet nicht statt? Erste deutsche Stadt hängt Ramadan-Beleuchtung auf! Das hat bei uns genau so wenig in der Öffentlichkeit zu suchen wie der Muezzinruf. Wir sind ein christlich geprägtes Land und das sollen und wollen wir auch bleiben! Deshalb müssen wir wachsam bleiben und uns gegend die fortschreitende Islamisierung unseres Landes zur Wehr setzen. Deswegen AfD. Deutschland aber normal.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 468

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