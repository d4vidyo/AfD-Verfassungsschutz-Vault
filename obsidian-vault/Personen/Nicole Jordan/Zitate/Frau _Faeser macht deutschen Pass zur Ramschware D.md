---
type: zitat
speaker: "[[Nicole Jordan]]"
date: 2022-11-28
topic: Menschenwürde
page_bfv: 203
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Nicole Jordan]] vom 28.11.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Frau #Faeser macht deutschen Pass zur Ramschware Die #Ampel-Parteien wollen den Bevölkerungsaustausch nun schnell forcieren. […] Diese Politik zeigt, wie man unser Land umkrempeln möchte.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 203

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