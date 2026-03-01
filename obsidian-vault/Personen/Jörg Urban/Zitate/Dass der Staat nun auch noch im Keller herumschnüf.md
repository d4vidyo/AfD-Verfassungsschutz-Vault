---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2023-05-25
topic: Demokratieprinzip
page_bfv: 648
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 25.5.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Dass der Staat nun auch noch im Keller herumschnüffeln will und im Zweifelsfall eine Heiz-Polizei aktiv wird, ist eine Vorstellung, die an die DDR und Orwells 1984 erinnert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 648

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