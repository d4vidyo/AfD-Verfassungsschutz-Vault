---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2023-02-22
topic: Menschenwürde
page_bfv: 201
source: 'Pressekonferenz'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 22.2.2023 veröffentlicht auf: 'Pressekonferenz'
> [!quote] Aussage
>Dann soll mir niemand mehr kommen und sagen, die These vom Bevölkerungsaustausch sei eine Verschwörungstheorie, dann ist das Verwaltungspraxis. [...] Und darum ist diese Art der Migration Gift für unseren Sozialstaat und deswegen muss das grundlegend geändert werden, wenn wir unser Land in absehbarer Zeit noch wiedererkennen wollen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 201

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