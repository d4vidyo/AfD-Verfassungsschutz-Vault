---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2023-01-27
topic: Menschenwürde
page_bfv: 299
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 27.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die schreckliche Attacke in einem Regionalzug zwischen Hamburg und Kiel hat ihren Weg in den medialen Mainstream gefunden. Doch der Doppelmord des mehrfach vorbestraften Migranten ist nur ein kleiner Teil eines fundamentalen Problems. Ob im Supermarkt, auf Spielplätzen, in der Tiefgarage oder in unseren Innenstädten - seit 2015 hat eine Kultur der Gewalt fast überall in Deutschland Einzug erhalten.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 299

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