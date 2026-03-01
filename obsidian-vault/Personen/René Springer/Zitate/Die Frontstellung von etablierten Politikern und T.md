---
type: zitat
speaker: "[[René Springer]]"
date: 2024-10-03
topic: Demokratieprinzip
page_bfv: 595
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 3.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Die Frontstellung von etablierten Politikern und Teilen des Staatsapparats gegen das eigene Volk ist ähnlich wie in der Spätphase der DDR. Am Tag der deutschen Einheit ist leider wenig Einheit in Deutschland zu spüren. Meinungsfreiheit ist notwendig, wenn dieser Staat sich nicht selbst delegitimieren will.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 595

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