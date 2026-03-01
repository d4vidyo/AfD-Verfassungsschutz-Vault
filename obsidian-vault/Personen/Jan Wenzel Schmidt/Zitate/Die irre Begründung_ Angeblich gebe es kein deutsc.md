---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2023-04-27
topic: Menschenwürde
page_bfv: 145
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 27.4.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Die irre Begründung: Angeblich gebe es kein deutsches Volk außer dem deutschen Staatsvolk (den Passdeutschen).

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 145

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