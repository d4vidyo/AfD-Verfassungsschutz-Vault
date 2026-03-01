---
type: zitat
speaker: "[[Matthias Moosdorf]]"
date: 2024-12-21
topic: Demokratieprinzip
page_bfv: 961
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Matthias Moosdorf]] vom 21.12.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Verbrecher der Kartellparteien sind für die Tat mitverantwortlich. Das moralisierende Wegschauen ist Teil einer Politik, in der Einheimische wie Fischfutter behandelt werden. Sie dürfen zahlen, sollen das Maul halten, wenn sie es nicht tun, schuriegelt man sie. Die kommende Bundestagswahl könnte diesem Irrsinn ein Ende machen, wenn... Ja, wenn die Deutschen endlich aufwachen würden. Stattdessen wieder nur dümmliches Framing.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 961

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