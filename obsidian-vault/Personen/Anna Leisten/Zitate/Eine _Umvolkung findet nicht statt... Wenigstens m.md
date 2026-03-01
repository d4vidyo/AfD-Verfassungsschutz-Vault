---
type: zitat
speaker: "[[Anna Leisten]]"
date: 2022-07-08
topic: Menschenwürde
page_bfv: 220
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Anna Leisten]] vom 8.7.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Eine #Umvolkung findet nicht statt... Wenigstens macht die #Regierung kein Geheimnis mehr aus ihrer antideutschen Politik!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 220

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