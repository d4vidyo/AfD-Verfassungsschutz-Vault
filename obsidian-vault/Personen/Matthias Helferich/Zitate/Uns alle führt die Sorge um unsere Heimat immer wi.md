---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2025-02-08
topic: Menschenwürde
page_bfv: 878
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 8.2.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Uns alle führt die Sorge um unsere Heimat immer wieder auf die Straße und natürlich am 23. Februar an die Wahlurne. Und was besorgt die meisten? [...] Es ist nicht die wirtschaftliche Lage unseres Landes, die besorgt uns auch. [...] Aber es besorgt uns, dass es in der Zukunft kein deutsches Volk mehr geben wird. Und deshalb gehen wir auf die Straße.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 878

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