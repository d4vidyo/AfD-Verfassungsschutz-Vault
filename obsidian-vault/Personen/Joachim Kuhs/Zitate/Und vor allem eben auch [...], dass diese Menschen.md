---
type: zitat
speaker: "[[Joachim Kuhs]]"
date: 2022-06-03
topic: Menschenwürde
page_bfv: 157
source: 'AUF1.TV'
status: Unbewertet
---

# Zitat: [[Joachim Kuhs]] vom 3.6.2022 veröffentlicht auf: 'AUF1.TV'
> [!quote] Aussage
>Und vor allem eben auch [...], dass diese Menschen [...] sich nicht integrieren und sich nicht assimilieren bei uns in unserer Gesellschaft. Das ist halt eben absolut notwendig.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 157

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