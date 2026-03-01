---
type: zitat
speaker: "[[Gerhard Vierfuß]]"
date: 2022-08-10
topic: Menschenwürde
page_bfv: 173
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Gerhard Vierfuß]] vom 10.8.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Unsere #Pseudo_Eliten haben d. ihre Politik des #Bevölkerungsaustauschs nicht nur unser Recht auf Bewahrung der #ethnokulturellen #Identität verletzt, s. auch die Grundlagen unseres #Rechtsstaats zerstört und den Staat #delegitimiert. Sie sind die wahren #Verfassungsfeinde.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 173

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