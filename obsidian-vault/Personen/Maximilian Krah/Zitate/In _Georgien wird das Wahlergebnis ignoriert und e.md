---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2024-12-06
topic: Menschenwürde
page_bfv: 946
source: 'X (ehemals Twitter), Repost'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 6.12.2024 veröffentlicht auf: 'X (ehemals Twitter), Repost'
> [!quote] Aussage
>In #Georgien wird das Wahlergebnis ignoriert und erklärt die pro-westliche Präsidentin, über das Ende ihrer Amtszeit einfach im Amt zu bleiben. In #Rumänien wird die Wahl kassiert, weil der Sieger nicht passt. Das ist ,unsere Demokratie' der Globalisten. Völker, wehrt Euch!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 946. Repost von Hans-Christoph Berndt

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