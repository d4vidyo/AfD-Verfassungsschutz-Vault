---
type: zitat
speaker: "[[Tomasz Froelich]]"
date: 2024-09-14
topic: Menschenwürde
page_bfv: 195
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Tomasz Froelich]] vom 14.9.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Nach Deutschland sollen nun 'IT-Spezialisten' aus #Kenia kommen, selbst wenn sie 'keine formale Qualifikation' haben. EU-Innenkommissarin Ylva Johansson hat schon vor vier Jahren angekündigt, wohin die Reise gehen soll: 'Wir müssen neue legale Wege auch für gering qualifizierte Zuwanderer finden, damit diese in die EU kommen können.' 250.000 davon sollen laut BBC nun allein aus Kenia nach Deutschland kommen. Was ist das anderes als ein Bevölkerungsaustausch ?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 195

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