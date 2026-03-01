---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2024-08-26
topic: Nationalsozialismus
page_bfv: 694
source: 'WELTplus'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 26.8.2024 veröffentlicht auf: 'WELTplus'
> [!quote] Aussage
>Wenn es etwas zu kritisieren gibt, dann machen wir das intern. Außerdem hat sich Höcke auch geändert. Das sehr provokante Element hat sich bei ihm abgeschwächt. Er macht einen hervorragenden Job in Thüringen. Die Strafprozesse finde ich lächerlich und fragwürdig.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 694

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