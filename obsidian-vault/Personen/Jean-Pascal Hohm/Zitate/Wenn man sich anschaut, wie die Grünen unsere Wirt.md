---
type: zitat
speaker: "[[Jean-Pascal Hohm]]"
date: 2023-02-16
topic: Menschenwürde
page_bfv: 212
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jean-Pascal Hohm]] vom 16.2.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wenn man sich anschaut, wie die Grünen unsere Wirtschaft an die Wand fahren und Millionen Menschen aus aller Herren Länder in unser Land holen, um unser Volk durch Fremde zu ersetzen, dann ist das für jeden ersichtlich.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 212

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