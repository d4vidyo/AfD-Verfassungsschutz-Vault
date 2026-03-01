---
type: zitat
speaker: "[[Gottfried Curio]]"
date: 2024-10-12
topic: Menschenwürde
page_bfv: 191
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Gottfried Curio]] vom 12.10.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>In wenigen Jahren wird durch diese Politik der Kipp-Punkt überschritten, wo die linksgrünen Deutschlandfeinde zusammen mit rasch eingebürgerten Syrern und Afghanen der angestammten deutschen Bevölkerung ihr Land unter den Füßen wegziehen sollen. Lassen wir das nicht zu, meine Damen und Herren, stellen wir uns dieser Veruntreuung unseres Vaterlands entgegen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 191

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