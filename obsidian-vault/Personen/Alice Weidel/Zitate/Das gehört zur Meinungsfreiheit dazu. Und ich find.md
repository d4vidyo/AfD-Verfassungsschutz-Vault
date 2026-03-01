---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2025-02-01
topic: Demokratieprinzip
page_bfv: 957
source: 'Videoeinspieler'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 1.2.2025 veröffentlicht auf: 'Videoeinspieler'
> [!quote] Aussage
>Das gehört zur Meinungsfreiheit dazu. Und ich finde, man darf das nicht verbieten. Wenn jemand die Meinung hat, dass ein anderer keine Ahnung hat - wie ein Kinderbuchautor von Wirtschaft und Energie - dann darf er doch "Schwachkopf" sagen. Was ist daran so falsch? Es ist nicht mal falsch, oder?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 957

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