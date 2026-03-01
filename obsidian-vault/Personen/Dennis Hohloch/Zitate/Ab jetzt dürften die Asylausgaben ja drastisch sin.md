---
type: zitat
speaker: "[[Dennis Hohloch]]"
date: 2024-12-08
topic: Menschenwürde
page_bfv: 907
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Dennis Hohloch]] vom 8.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ab jetzt dürften die Asylausgaben ja drastisch sinken. Aber auch ein schwerer Rückschlag für die heimische Messerindustrie. #Syrien #Assad

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 907

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