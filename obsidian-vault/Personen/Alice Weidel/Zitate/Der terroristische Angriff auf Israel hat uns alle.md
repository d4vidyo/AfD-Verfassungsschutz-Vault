---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2023-10-12
topic: Menschenwürde
page_bfv: 529
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 12.10.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der terroristische Angriff auf Israel hat uns alle tief geschockt. Die entschlossene Reaktion auf die Gräueltaten war notwendig und berechtigt. Deutschlands Beitrag muss sein, radikalislamistische Netzwerke zu zerschlagen und nicht weiter zu fördern.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 529

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