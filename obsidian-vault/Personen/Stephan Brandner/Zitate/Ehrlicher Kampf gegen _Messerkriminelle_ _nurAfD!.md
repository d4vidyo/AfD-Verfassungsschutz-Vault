---
type: zitat
speaker: "[[Stephan Brandner]]"
date: 2023-03-08
topic: Menschenwürde
page_bfv: 290
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Stephan Brandner]] vom 8.3.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ehrlicher Kampf gegen #Messerkriminelle: #nurAfD!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 290

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