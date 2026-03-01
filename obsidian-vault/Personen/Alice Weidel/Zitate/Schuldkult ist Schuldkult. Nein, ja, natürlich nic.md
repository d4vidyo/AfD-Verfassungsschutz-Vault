---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2025-02-02
topic: Nationalsozialismus
page_bfv: 979
source: 'Talkshow'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 2.2.2025 veröffentlicht auf: 'Talkshow'
> [!quote] Aussage
>Schuldkult ist Schuldkult. Nein, ja, natürlich nicht. Aber es ist ja auch völlig egal. Also mittlerweile ist ja auch sämtliche Sachen, die man nicht mehr sagen darf. Man darf Schwachkopf nicht mehr sagen zu einem totalen unfähigen Energie- und Wirtschaftsminister.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 979

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