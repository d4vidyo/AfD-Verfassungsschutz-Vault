---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-11-07
topic: Menschenwürde
page_bfv: 213
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 7.11.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Es war und ist ein Hauptanliegen meines eigenen politischen Wirkens, denn: Ich liebe mein Land und mein Volk. Ihm gehört meine Treue. 'Wir protestieren gegen die planmäßige Ersetzung der deutschen Bevölkerung durch Migranten.'

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 213

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