---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2023-01-06
topic: Demokratieprinzip
page_bfv: 649
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 6.1.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Statt sich für Verhandlungen einzusetzen, bringt diese fanatische, größenwahnsinnige und ungebildete Hasardeurregierung unser Land an den Rand eines 3. Weltkrieges.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 649

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