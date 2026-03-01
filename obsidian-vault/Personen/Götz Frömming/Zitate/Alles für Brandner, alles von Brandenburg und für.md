---
type: zitat
speaker: "[[Götz Frömming]]"
date: 2024-09-13
topic: Nationalsozialismus
page_bfv: 695
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Götz Frömming]] vom 13.9.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Alles für Brandner, alles von Brandenburg und für Brandenburg! Ich wünsche noch viel Erfolg!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 695

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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