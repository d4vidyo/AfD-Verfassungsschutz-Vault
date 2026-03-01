---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2023-11-26
topic: Demokratieprinzip
page_bfv: 538
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 26.11.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Hat Ihre Gemeinde auch z. B. einen hochdotierten Klimamanager? Fragen Sie doch mal nach, was dieser Posten an Besoldung wert ist. Mit 'prima Klima' kann weltweit viel Geld verdient und eine Weltregierung installiert werden, die den Menschen, Demokratie und Freiheit dem Klima unterordnet.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 538

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