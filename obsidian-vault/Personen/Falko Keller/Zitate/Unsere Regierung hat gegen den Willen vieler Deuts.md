---
type: zitat
speaker: "[[Falko Keller]]"
date: 2021-06-27
topic: Menschenwürde
page_bfv: 320
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Falko Keller]] vom 27.6.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Unsere Regierung hat gegen den Willen vieler Deutscher all diese Illegalen einreisen lassen. Die Bundesregierung wollte diesen angeblich in großer Not befindlichen Menschen helfen. Was ist der Dank? Sie töten, vergewaltigen, stehlen, schlagen unsere Kinder, schmarotzen sich durch unser Sozialsystem. [...] Immer wieder sind es die Unschuldigen, die von den Illegalen getötet werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 320

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