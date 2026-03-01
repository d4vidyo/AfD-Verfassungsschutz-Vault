---
type: zitat
speaker: "[[Alexander Jungbluth]]"
date: 2024-10-07
topic: Sonstiges
page_bfv: 699
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Alexander Jungbluth]] vom 7.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Rechte die Kampfsport machen beschützen Frauen und Töchter. [...] #Hachenburg #Fassfabrik

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 699

**Verfassungsschutz Kategorisierung:** Sonstiges.

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