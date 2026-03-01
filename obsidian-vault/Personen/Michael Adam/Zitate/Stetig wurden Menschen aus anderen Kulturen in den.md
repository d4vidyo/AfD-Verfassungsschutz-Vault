---
type: zitat
speaker: "[[Michael Adam]]"
date: 2023-01-13
topic: Menschenwürde
page_bfv: 155
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Michael Adam]] vom 13.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Stetig wurden Menschen aus anderen Kulturen in den deutschen Kulturkreis aufgenommen und die Aufgenommenen assimilierten sich meist schnell im deutschen 'Volkskörper'.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 155

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