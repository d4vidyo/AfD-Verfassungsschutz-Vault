---
type: zitat
speaker: "[[René Springer]]"
date: 2023-06-08
topic: Menschenwürde
page_bfv: 198
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 8.6.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Jede #Asylreform, die nicht #FestungEuropa und #Nullzuwanderung bedeutet, ist zu wenig. Die Politik des Bevölkerungsaustauschs muss endlich gestoppt werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 198

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