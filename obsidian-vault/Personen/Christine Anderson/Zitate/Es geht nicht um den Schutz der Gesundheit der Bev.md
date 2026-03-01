---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2022-06-22
topic: Demokratieprinzip
page_bfv: 621
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 22.6.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Es geht nicht um den Schutz der Gesundheit der Bevölkerung, sondern um den Schutz von Regierungen und Politik vor unangenehmen Bürgern und deren legitime Nutzung demokratischer Freiheiten und Grundrechten. Demokratische Beteiligung wird dann nur denjenigen Bürgern gewährt, denen zuvor von der Regierung einen "Digitalen Grundrechtsgutschein" ausgestellt wurde. Alle anderen werden stattdessen direkt in einen "Demokratie-Lockdown" geschickt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 621

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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