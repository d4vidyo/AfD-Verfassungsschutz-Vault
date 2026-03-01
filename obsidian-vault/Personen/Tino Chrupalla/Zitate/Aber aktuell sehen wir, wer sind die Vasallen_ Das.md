---
type: zitat
speaker: "[[Tino Chrupalla]]"
date: 2023-04-15
topic: Demokratieprinzip
page_bfv: 553
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Tino Chrupalla]] vom 15.4.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Aber aktuell sehen wir, wer sind die Vasallen? Das ist Baerbock, das ist Merz, das ist Röttgen. Das sind die Vasallen Amerikas, die munter weitermachen und das wird uns ins Verderben führen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 553

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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