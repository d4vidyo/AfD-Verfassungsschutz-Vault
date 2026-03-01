---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2024-06-26
topic: Sonstiges
page_bfv: 706
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 26.6.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Politik ist der Kampf um die Deutungshoheit. Wer meint, diesen Kampf alleine in den Parlamenten und Talkshows gewinnen zu können, hat schon verloren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 706

**Verfassungsschutz Kategorisierung:** Sonstiges.

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