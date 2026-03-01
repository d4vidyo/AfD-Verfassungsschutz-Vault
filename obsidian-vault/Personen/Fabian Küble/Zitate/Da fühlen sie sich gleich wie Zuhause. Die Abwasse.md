---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2024-10-14
topic: Menschenwürde
page_bfv: 386
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 14.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Da fühlen sie sich gleich wie Zuhause. Die Abwasserentsorgung ist in vielen Herkunftsstaaten auch nicht geregelt. Oft regelt da der Busch. Die Afrikanisierung Deutschlands schreitet voran. Wer halb Afrika aufnimmt hilft eben nicht Afrika, sondern wird selbst Afrika.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 386. Kommentar zu einem Medienbericht der Welt

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