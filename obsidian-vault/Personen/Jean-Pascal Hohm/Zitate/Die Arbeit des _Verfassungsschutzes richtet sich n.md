---
type: zitat
speaker: "[[Jean-Pascal Hohm]]"
date: 2023-04-27
topic: Menschenwürde
page_bfv: 207
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Jean-Pascal Hohm]] vom 27.4.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die Arbeit des #Verfassungsschutzes richtet sich nicht gegen einzelne Organisationen, sondern gegen das Deutsche Volk. Jeglicher positive Bezug zum Eigenen wird kriminalisiert. So versucht man die Abwehrkräfte des Volkes gegen den stattfindenden Austausch zu schwächen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 207

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